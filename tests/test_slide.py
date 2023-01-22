import matplotlib.pyplot as plt
import numpy as np
from parapyro.presentation import Presentation
from parapyro.slides.object import imageobject_from_pyplot
from parapyro.slides.page import Page


x = np.random.rand(50)
y = np.random.rand(50)

fig, ax = plt.subplots(figsize=(16, 9), layout='constrained')
ax.scatter(x=x, y=y)
obj = imageobject_from_pyplot(fig, 'clown')

pres = Presentation("test_name")
pres.add_page(Page("example page", "oh this content is nasty good yes"))
pres.add_page(Page("example plot", obj.compile()))
pres.compile()
pres.render()