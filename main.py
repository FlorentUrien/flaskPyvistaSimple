"""Simple flask app to display static images generated from pyvista.

Expected paths:
static_ex/
└── app.py
    templates/
    └── index.html

"""
import os

from flask import Flask, escape, render_template, request

import pyvista
import subprocess
import vtk

static_image_path = os.path.join('static', 'images')
if not os.path.isdir(static_image_path):
    os.makedirs(static_image_path)

app = Flask(__name__)


def activate_virtual_framebuffer():
    '''
    Activates a virtual (headless) framebuffer for rendering 3D
    scenes via VTK.

    Most critically, this function is useful when this code is being run
    in a Dockerized notebook, or over a server without X forwarding.

    * Requires the following packages:
      * `sudo apt-get install libgl1-mesa-dev xvfb`
    '''

    vtk.OFFSCREEN = True
    os.environ['DISPLAY'] = ':99.0'

    commands = ['Xvfb :99 -screen 0 1024x768x24 > /dev/null 2>&1 &',
                'sleep 3',
                'exec "$@"']

    for command in commands:
        subprocess.call(command, shell=True)


@app.route("/")
def index():
    print("11111111111")
    return render_template('index.html')


@app.route("/getimage")
def get_img():
    """Generate a screenshot of a simple pyvista mesh.

    Returns
    -------
    str
        Local path within the static directory of the image.

    """
    # get the user selected mesh option
    meshtype = request.args.get('meshtype')
    if meshtype == 'Sphere':
        mesh = pyvista.Sphere()
    elif meshtype == 'Cube':
        mesh = pyvista.Cube()
    elif meshtype == 'Bohemian Dome':
        mesh = pyvista.ParametricBohemianDome()
    elif meshtype == 'Cylinder':
        mesh = pyvista.Cylinder()
    else:
        # invalid entry
        raise ValueError('Invalid Option')

    # generate screenshot
    filename = f'{meshtype}.png'
    filepath = os.path.join(static_image_path, escape(filename))
    mesh.plot(off_screen=True, window_size=(300, 300), screenshot=filepath)
    return os.path.join('images', filename)


if __name__ == '__main__':
    print("000000")
    activate_virtual_framebuffer()
    print("aaaaa")
    app.run(host='0.0.0.0')
