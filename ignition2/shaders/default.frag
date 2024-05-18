#version 460

layout (location = 0) out vec4 fragColor;

void main() {
    vec3 col = vec3(1, 1, 1);
    fragColor = vec4(col, 1.0);
}
