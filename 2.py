import plotly.graph_objects as go
import numpy as np

# Generate random data
np.random.seed(42)
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

# Create a 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=5,
        color=z,  # Set color to the z value
        colorscale='Viridis',  # Color scale
        opacity=0.8
    )
)])

# Update layout
fig.update_layout(
    title='3D Scatter Plot',
    scene=dict(
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        zaxis_title='Z Axis'
    )
)

# Show the plot
fig.show()
