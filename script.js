const gallery = document.getElementById('gallery');
const lightbox = document.getElementById('lightbox');
const lightboxImage = document.getElementById('lightbox-image');

const artworks = [
  "image1.png",
  "image2.png",
  "image3.png",
  "image4.png",
  "image5.png",
  "image6.png",
  "image7.png",
  "image8.png",
  "image9.png",
  "image10.png",
  "image11.png",
  "image12.png",
  "image13.png",
  "image14.png",
  "image15.png",
  "image16.png",
  "image17.png",
  "image18.png",
  "image19.png",
  "image20.png",
  "image21.png",
  "image22.png",
  "image23.png",
  "image24.png",
  "image25.png",
  "image26.png",
  "image27.png",
  "image28.png",
  "image29.png"
]

artworks.forEach((artwork, index) => {
  const thumbnail = `thumbnails/image${index + 1}.png`;
  const artworkElement = document.createElement('div');
  artworkElement.className = 'artwork';
  artworkElement.innerHTML = `<img src="${thumbnail}" alt="Artwork ${index+1}" onclick="openLightbox('${artwork}')">`;
  gallery.appendChild(artworkElement);
});

function openLightbox(artwork) {
  lightboxImage.src = `images/${artwork}`;
  lightbox.style.display = 'block';
}

function closeLightbox() {
  lightbox.style.display = 'none';
}