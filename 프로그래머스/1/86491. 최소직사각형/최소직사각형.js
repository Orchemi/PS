function solution(sizes) {
    const turnedSizes = sizes.map((size) => size.sort((a, b) => a - b))
    const maxWidth = Math.max(...turnedSizes.map((size) => size[0]));
    const maxHeight = Math.max(...turnedSizes.map((size) => size[1]));
    return maxWidth * maxHeight;
}