#version 460

layout (location = 0) in vec2 in_pos;

uniform mat4 model_m;
uniform mat4 view_m;
uniform mat4 proj_m;

void main() {
    gl_Position = proj_m * view_m * model_m * vec4(in_pos, -1.0, 1.0);
}
