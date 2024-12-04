#version 330 core

layout (location = 0) in vec3 vertexPos;
layout (location = 1) in vec2 vertexTexCoord;

out vec2 uvs;
uniform float time;

void main()
{
    float scale = 1.0 + 0.5 * sin(time*2);

    vec3 scaledPos = vertexPos * scale;

    uvs = vertexTexCoord;
    gl_Position = vec4(scaledPos, 1.0);
}