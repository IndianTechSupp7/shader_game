#version 330 core

in vec3 fragmentColor;
in vec2 uvs;

uniform sampler2D imageTexture;
uniform float time;
uniform float offset;

out vec4 color;

void main() {
    vec2 uv = uvs;
    vec3 tex_color = texture(imageTexture, uvs).rgb;
    float pulse = pow(sin(uv.x + time + offset), 2)*0.3;
    color = vec4(tex_color + pulse, 1.0);
}