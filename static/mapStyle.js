function updateStyles(areaNumber) {
    var likes = getLikesForArea(areaNumber);
    var areaElement = document.querySelector('.area' + areaNumber);

    areaElement.classList.remove('fill-1', 'fill-2', 'fill-3');

    if (likes <= 1) {
        areaElement.classList.add('fill-1');
    } else if (likes <= 2) {
        areaElement.classList.add('fill-2');
    } else {
        areaElement.classList.add('fill-3');
    }
}