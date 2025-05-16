from union import ImageSpec

container_image = ImageSpec(
    name="example-image",
    builder="union",
    requirements="./requirements.txt",
)

app_image = ImageSpec(
    name="union-serve-keras-fastapi",
    packages=["union-runtime>=0.1.10", "tensorflow", "fastapi[standard]", "pillow"],
    builder="union",
)
