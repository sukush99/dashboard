import streamlit as st 
from streamlit_elements import elements, mui, html,dashboard
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from streamlit_lightweight_charts import renderLightweightCharts


def main():
    st.set_page_config(layout="wide")
    with elements("dashboard"):

    # You can create a draggable and resizable dashboard using
    # any element available in Streamlit Elements.


    # First, build a default layout for every element you want to include in your dashboard

        layout = [
            # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
            dashboard.Item("item1", 0, 0, 2, 1.5),
            dashboard.Item("item2", 0, 0, 2, 2),
            dashboard.Item("item3", 0, 0, 2, 2),
            dashboard.Item("second_item", 2, 0, 8, 5.5, isDraggable=False, moved=False),
            dashboard.Item("third_item", 12, 2, 2, 5.5, isDraggable=False, moved=False, isResizable=True),
        ]

        # Next, create a dashboard layout using the 'with' syntax. It takes the layout
        # as first parameter, plus additional properties you can find in the GitHub links below.

        with dashboard.Grid(layout):
            mui.Paper("Item1", key="item1")
            mui.Paper("Item2", key="item2")
            mui.Paper("Item3", key="item3")
            mui.Paper("Second item (cannot drag)", key="second_item")
            mui.Paper("Quick Snap Shot", key="third_item")

        # If you want to retrieve updated layout values as the user move or resize dashboard items,
        # you can pass a callback to the onLayoutChange event parameter.



if __name__ == "__main__":
    main()
