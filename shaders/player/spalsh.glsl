#version 330 core

in vec3 fragmentColor;
in vec2 uvs;

out vec4 color;

uniform sampler2D imageTexture;
uniform float time;


void main() {
    vec2 uv = (uvs*2)-1;
    float c = length(uv);
    uv += vec2(cos(time), sin(time)) * c;
    color = vec4(uv, 0., 1.);
}