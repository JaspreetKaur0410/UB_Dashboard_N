import streamlit as st
import pandas as pd 
import numpy as np
from query import *
from main import *
from all_queries import *
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

def convert_to_pd(query_var):
    return pd.DataFrame(query_var)

# start - USER DATA
df_data_users=convert_to_pd(get_users_data_filters())
# AgGrid(df_data_users)

gb = GridOptionsBuilder.from_dataframe(df_data_users)
gb.configure_pagination() #Add pagination
gb.configure_side_bar() #Add a sidebar
gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
gridOptions = gb.build()

grid_response = AgGrid(
    df_data_users,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='material', #Add theme color to the table
    enable_enterprise_modules=True, 
    height=500,
    width='100%',
    reload_data=True,
    custom_css={
        "#gridToolBar": {
            "padding-bottom": "0px !important",
        }
    }
)

data = grid_response['data']
selected = grid_response['selected_rows'] 
df = pd.DataFrame(selected) #Pass the selected rows to a new dataframe df




# end - USER DATA