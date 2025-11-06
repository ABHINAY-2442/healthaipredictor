import plotly.express as px
import plotly.graph_objects as go

# Data
diseases = ["Diabetes", "Heart Disease", "Parkinson's"]
accuracy = [79.5, 85.0, 91.0]
algorithm = ["SVM", "Logistic Regression", "SVM"]

# Brand colors for the bars
colors = ["#1FB8CD", "#DB4545", "#2E8B57"]  # Using brand colors instead

# Create horizontal bar chart
fig = go.Figure()

# Add bars with custom colors
for i, (disease, acc, color) in enumerate(zip(diseases, accuracy, colors)):
    fig.add_trace(go.Bar(
        y=[disease], 
        x=[acc],
        orientation='h',
        marker_color=color,
        text=[f"{acc}%"],
        textposition='outside',
        name=disease,
        showlegend=False
    ))

# Update layout
fig.update_layout(
    title="Model Accuracy Comparison",
    xaxis_title="Accuracy (%)",
    yaxis_title="Disease",
    xaxis=dict(range=[0, 100])
)

# Update traces to prevent clipping
fig.update_traces(cliponaxis=False)

# Save as both PNG and SVG
fig.write_image("accuracy_chart.png")
fig.write_image("accuracy_chart.svg", format="svg")

print("Chart saved successfully!")