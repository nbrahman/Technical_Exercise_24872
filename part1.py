# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 10:30:20 2024

@author: wb584620
"""

import traceback
import pandas as pd
import wbgapi as wb
from datetime import datetime
import plotly.express as px
import plotly

class clsPart1:
    """
    Function to read World Bank Group data using wbgapi package.
    It accepts following parameters:
        strIndCode (string) - An Indicator code indicating Economic Time Series to be read from WBG Databank
    It returns a dictionary object with dataframe with data from file, and exceptions if any.
    """
    def __readWBGData (self, paramStrIndCode, paramIntFromYear=1960, paramIntDB=2) -> dict:
        dfData = None
        dictRet = {}
        strException = ""
        try:
            dfData = wb.data.DataFrame(series=paramStrIndCode, time=range(paramIntFromYear, datetime.now().year), 
                                       economy=["WLD", "UMC", "LMC", "HIC", "LIC"], 
                                       skipBlanks=True, labels=True, numericTimeKeys=True, db=paramIntDB)
            dfData = dfData.reset_index()
            lstCols = list(dfData.columns)
            dfData = dfData.melt(id_vars=[lstCols[0], lstCols[1]])
            dfData.columns = ["Economy Code", "Economy Name", "Year", "Value"]

            if dfData.empty==False:
                dfData.fillna("")
                dfData["Year"] = pd.to_numeric(dfData["Year"])

            cht = px.line(dfData, x="Year", y="Value", color="Economy Name", 
                          labels={"Year": "Years", "Value": "People using basic sanitation services (% of population) (SH.STA.BASS.ZS)"}, 
                          title="<b>Access to basic sanitation services</b>",
                          category_orders={"Economy Name": ["Low income", "Lower middle income", "Upper middle income", "High income", "World"]},
                          markers=True)
            cht.update_layout(legend={"orientation":"h", "yanchor":"bottom"}, 
                              title={"xanchor":"center", "yanchor":"top", "y":0.95, "x":0.5, "font":{"size":20}},
                              paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                              hoverlabel={"bgcolor":"rgba(255,255,255,255)", })
            cht.update_xaxes(ticks="inside", showgrid=False, showline=True, linewidth=1, linecolor="black", 
                             zeroline=True, zerolinewidth=1, zerolinecolor="black")
            cht.update_yaxes(ticks="inside", col=1, showgrid=False, showline=True, linewidth=1, linecolor="black", 
                             zeroline=True, zerolinewidth=1, zerolinecolor="black", range=[0, 100])
            cht.show()
            cht.write_image(".\\test1.jpg")
        except Exception as e:
            self.__addErrors("clsPart1: Error - Unable to read data from World Bank Group Data Bank\nclsPart1: Exception details\n{}\n{}\n{}\n{}\n".format(type(e), e.args, e, traceback.format_exc()))
        finally:
            #print(dfData.shape)
            #print(dfData.columns)
            dictRet["data"] = dfData
            dictRet["exception"] = strException
            return dictRet

    """
    Function to display errors encoutnered during processing.
    It displays the errors on screen
    """
    def __addErrors (self, strErrorMessage, strCountryName="Generic", strYear=""):
        lstErrors = self.__dictErrors.get("{}-{}".format(strCountryName, strYear), [])
        lstErrors.append(strErrorMessage)
        self.__dictErrors["{}-{}".format(strCountryName, strYear)] = list(set(lstErrors))

    """
    Function to display errors encoutnered during processing.
    It displays the errors on screen
    """
    def displayErrors (self, blnDisplayOnlyErrors=True):
        lstK = list(self.__dictErrors.keys())
        lstK.sort()
        for k in lstK:
            if blnDisplayOnlyErrors==False:
                print("\n".join(self.__dictErrors[k]))
            else:
                for s in list(self.__dictErrors[k]):
                    if "Error - " in s:
                        print(s,end="\n")


    """
    Constructor to initialize Debt Dashboard objects. It accepts
        paramStrCntryFile: Country Metadata File Name along with Full Path.
        paramStrDestFileName: Final Output File Name along with Full Path.
        paramIntFromYear: Starting Year to extract data.
        paramIntToYear: Ending Year to extract data.
    """
    def __init__(self, paramIntFromYear=2000):
        self.__dictErrors = {}
        dictData = self.__readWBGData("SH.STA.BASS.ZS", paramIntFromYear, paramIntDB=2)

def main():
    try:
        obj = clsPart1(paramIntFromYear=1960)
    finally:
        obj.displayErrors()


if __name__ == "__main__":
    main()