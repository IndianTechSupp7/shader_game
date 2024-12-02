#version 330 core

in vec3 fragmentColor;
in vec2 uvs;

out vec4 color;

uniform sampler2D imageTexture;

void main() {
    color = vec4(uvs, 0., 1.);
}