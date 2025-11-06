import plotly.graph_objects as go
import plotly.express as px

# Create a flowchart using Plotly
fig = go.Figure()

# Define node positions for the flowchart
nodes = {
    'Start': (0.5, 1.0),
    'Home': (0.5, 0.9),
    'Select': (0.5, 0.8),
    'Diabetes': (0.2, 0.7),
    'Heart': (0.5, 0.7),
    'Parkinson': (0.8, 0.7),
    'Validate': (0.5, 0.6),
    'Process': (0.5, 0.5),
    'Model': (0.5, 0.4),
    'Risk': (0.5, 0.3),
    'Decision': (0.5, 0.2),
    'High': (0.3, 0.1),
    'Low': (0.7, 0.1),
    'Another': (0.5, 0.05),
    'End': (0.8, 0.0)
}

# Add nodes with different colors based on type
for node, (x, y) in nodes.items():
    if node in ['Start', 'End']:
        color = '#2E8B57'  # Green for start/end
        symbol = 'circle'
    elif node in ['Select', 'Decision', 'Another']:
        color = '#D2BA4C'  # Yellow for decisions
        symbol = 'diamond'
    elif node in ['Diabetes', 'Heart', 'Parkinson', 'High', 'Low']:
        color = '#B3E5EC'  # Light blue for input/output
        symbol = 'square'
    else:
        color = '#1FB8CD'  # Blue for processes
        symbol = 'square'
    
    fig.add_trace(go.Scatter(
        x=[x], y=[y],
        mode='markers+text',
        marker=dict(size=30, color=color, symbol=symbol),
        text=node.replace('_', '<br>'),
        textposition='middle center',
        textfont=dict(size=10, color='white' if color in ['#2E8B57', '#1FB8CD'] else 'black'),
        showlegend=False,
        hoverinfo='skip'
    ))

# Add arrows/connections
connections = [
    ('Start', 'Home'),
    ('Home', 'Select'),
    ('Select', 'Diabetes'),
    ('Select', 'Heart'),
    ('Select', 'Parkinson'),
    ('Diabetes', 'Validate'),
    ('Heart', 'Validate'),
    ('Parkinson', 'Validate'),
    ('Validate', 'Process'),
    ('Process', 'Model'),
    ('Model', 'Risk'),
    ('Risk', 'Decision'),
    ('Decision', 'High'),
    ('Decision', 'Low'),
    ('High', 'Another'),
    ('Low', 'Another'),
    ('Another', 'Home'),
    ('Another', 'End')
]

for start, end in connections:
    x_start, y_start = nodes[start]
    x_end, y_end = nodes[end]
    
    fig.add_trace(go.Scatter(
        x=[x_start, x_end],
        y=[y_start, y_end],
        mode='lines',
        line=dict(color='#333333', width=2),
        showlegend=False,
        hoverinfo='skip'
    ))

# Update layout
fig.update_layout(
    title='AI Health Predictor System Workflow',
    xaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[-0.1, 1.1]),
    yaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[-0.1, 1.1]),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Save as PNG and SVG
fig.write_image('ai_health_predictor.png')
fig.write_image('ai_health_predictor.svg', format='svg')

print("AI Health Predictor flowchart created successfully!")
print("Files saved as ai_health_predictor.png and ai_health_predictor.svg")