document.addEventListener('DOMContentLoaded', function () {
    const stars = document.querySelectorAll('.rating input');
    const ratingMessage = document.getElementById('ratingMessage');

    stars.forEach((star) => {
        star.addEventListener('click', function () {
            const ratingValue = parseInt(this.value);
            const pluralSuffix = ratingValue === 1 ? '' : 's';
            ratingMessage.textContent = 'You rated ' + ratingValue + ' star' + pluralSuffix + '.';
            updateReviewStars(ratingValue);
        });
    });

    function updateReviewStars(stars) {
        const reviewStars = document.querySelectorAll('.review-stars');
        reviewStars.forEach((reviewStar) => {
            reviewStar.textContent = stars + ' star' + (stars === 1 ? '' : 's');
        });
    }
});
