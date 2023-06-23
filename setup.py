from setuptools import setup

setup(name="eqxhubtest",
      description="Test repo",
      version="0.1",
      license="MIT",
      author="Peter Melchior",
      author_email="peter.m.melchior@gmail.com",
      py_modules=["eqxhubtest"],
      url="https://github.com/pmelchior/eqxhubtest",
      requires=["jax", "equinox"]
)

