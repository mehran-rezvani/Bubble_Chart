import plotly.express as px
import plotly.graph_objects as go

# Defining the data:
df = px.data.gapminder()
df_2007 = df[df.year==2007]

# Creating bubble chart:
fig = px.scatter(df_2007, y="lifeExp", x="gdpPercap", size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=100,
                 color_discrete_sequence=px.colors.qualitative.Plotly)

# Customizing chart layout:
fig.update_layout(autosize=False, width=800, height=400,
                  title_text='Countries Population, Life Expectancy And GDP per Capita', title_x=0.5,
                  annotations=[go.layout.Annotation(text="2007", x=2.7, y=80,
                               showarrow=False, font={"color": '#c48efd', "size": 50})])

fig.show()
