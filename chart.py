from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.legends import Legend
from plant import Plant
from plant_data_handling import get_plants_list
import csv

def create_chart_pdf():
    pdf_file = "chart.pdf"
    drawing = Drawing(1000,500)
    line_chart = HorizontalLineChart()
    lines_colours = [colors.blue, colors.pink, colors.yellow, colors.orange, colors.black, colors.magenta, colors.cyan]

    # initiating empty objects for data
    my_plants = get_plants_list("my_plants.csv")
    dates = []
    plants_data = []
    legend_names = []

    # creating empty elements for new data arrays
    for row in my_plants:
        plants_data.append({"name": row["Name"], "data" :[]})
        legend_names.append([])

    # appending data object with measurments and dates object with dates
    with open("plants_history.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for i, plant in enumerate(plants_data):
                if row["name"] == plant["name"]:
                    plants_data[i]["data"].append(int(row["Moisture reading"]))
                    date = row["Time of measurments"].split(" ")[0]
                    if date not in dates:
                        dates.append(date)

    # creating data object that's suitable format for the library
    data = []
    for plant in plants_data:
        if plant['data']:
            data.append(plant['data'])
    # applying different colours for the chart lines and legend
    i = 0
    while i < len(data):
        try:
            line_chart.lines[i].strokeColor = lines_colours[i]
            legend_names[i].append(lines_colours[i])
        except IndexError:
            line_chart.lines[i].strokeColor = lines_colours[0]
            legend_names[i].append(lines_colours[0])
        i += 1

    # creating legend object and it's settings
    for i,row in enumerate(plants_data):
        legend_names[i].append(row["name"])
    
    line_chart.categoryAxis.categoryNames = dates
    legend = Legend()
    legend.x = 600
    legend.y = 470
    legend.alignment = 'right'
    legend.colorNamePairs = legend_names

    # line chart position and setting
    line_chart.x = 50
    line_chart.y = 50
    line_chart.width = 900
    line_chart.height = 330
    line_chart.data = data
    line_chart.lines.strokeWidth = 3
    line_chart.valueAxis.valueMin = Plant.air_moisture
    line_chart.valueAxis.valueMax = Plant.water_moisture
    line_chart.valueAxis.valueStep = 50
    line_chart.categoryAxis.labels.boxAnchor = 'ne'
    line_chart.categoryAxis.labels.dx = 0
    line_chart.categoryAxis.labels.dy = -10
    line_chart.categoryAxis.labels.angle = 0

    # creating pdf title
    text = String(50, 440, 'Your plants soil moisture over time', fontSize=20, fillColor=colors.black, fontName = "Helvetica-Bold")

    drawing.add(text)
    drawing.add(line_chart, '')
    drawing.add(legend)
    renderPDF.drawToFile(drawing, pdf_file, '')
create_chart_pdf()