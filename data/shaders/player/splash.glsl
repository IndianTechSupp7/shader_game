#version 330 core

in vec3 fragmentColor;
in vec2 uvs;

out vec4 color;

uniform sampler2D imageTexture;
uniform float time;
uniform vec2 offset = vec2(0, 0);

vec2 rot(vec2 uv, float r) {
    mat2x2 rot_mat = mat2x2(cos(r), sin(r), -sin(r), cos(r));
    return uv * rot_mat;
}

void main() {
    vec2 uv = uvs.xy + offset;
    vec3 col = 0.5 + 0.5*cos(time+uv.xyx+vec3(0,2,4));
    color = vec4(col, 1.);
}