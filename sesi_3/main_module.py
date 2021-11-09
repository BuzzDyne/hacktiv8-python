import importlib

from models import person as p
from models.person import display as d

d(p.name)

d(p.devices[-1])

importlib.reload(p)