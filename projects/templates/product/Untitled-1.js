
        <section class="container mt-4">
            <div class="row">
                <div class="col-4 mt-3">
                <div id="ProductsThumbnailSlider" class="carousel carousel-dark slide carousel-fade" data-bs-ride="true">
                    <div class="carousel-indicators">
                        <button type="button" data-bs-target="#ProductsThumbnailSlider" data-bs-slide-href="0" class="active" aria-current="true" aria-label="Slide 1">
                        </button>
                        <button type="button" data-bs-target="#ProductsThumbnailSlider" data-bs-slide-href="1"  aria-label="Slide 2">
                        </button>
                        <button type="button" data-bs-target="#ProductsThumbnailSlider" data-bs-slide-href="2"  aria-label="Slide 3">
                        </button>

                    </div>
                <div class="carousel-inner">
                    <div class="carousel-item active">
                            <img src="{{product_details.prdMainImage.url}}" class="img-thumbnail mb-5" alt="..."/>
                    </div>
                    <div class="carousel-item">
                            <img src="{{product_details.prdMainImage.url}}" class="img-thumbnail" alt="..." />
                    </div>
                    <div class="carousel-item">
                            <img src="{{product_details.prdMainImage.url}}" class="img-thumbnail" alt="..." />
                    </div>
                </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#ProductsThumbnailSlider" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#ProductsThumbnailSlider" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                </div>                    
                </div>
                <div class="col-8">
                    <h3>Product Title</h3>
                    <p>    "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod "
                            "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim "
                            "veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea "
                            "commodo consequat. Duis aute irure dolor in reprehenderit in voluptate "
                            "velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint "
                            "occaecat cupidatat non proident, sunt in culpa qui officia deserunt "
                            "mollit anim id est laborum."</p>
                    <h5 class="card-title">Price: SR 500</h5>
                    <p class="mt-3">
                        <a title="Demo" href="_blank" class="btn btn-dark">
                            <i class="fa-brands fa-aws"></i> Demo
                        </a>
                        <button title="add to cart" class="btn btn-success ms-1">
                            <i class="fa-solid fa-cart-plus"></i> Add to cart
                        </button>
                        <button title="Buy Now" class="btn btn-primary ms-1">
                            <i class="fa-solid fa-bag-shopping"></i> Buy Now
                        </button>
                        <button title="add to wishlist" class="btn btn-danger ms-1">
                            <i class="fa fa-heart"></i> Wishlist
                        </button>
                    </p>
                    <div class="producttags mt-4">
                        <h5 class="">Tags</h5>
                        <p>
                            <a href="#" class="badge bg-info text-white me-1">Python</a>
                            <a href="#" class="badge bg-info text-white me-1">Django</a>
                            <a href="#" class="badge bg-info text-white me-1">JavaScript</a>
                            <a href="#" class="badge bg-info text-white me-1">Python</a>
                            <a href="#" class="badge bg-info text-white me-1">Django</a>
                            <a href="#" class="badge bg-info text-white me-1">JavaScript</a>
                        </p>
                    </div>
                </div>
            </div>
                <h3 class="mt-5 mb-3">Related Products</h3>
                <div id="relatedProductsSlider" class="carousel carousel-dark slide" data-bs-ride="true">
                    <div class="carousel-indicators">
                        <button type="button" data-bs-target="#relatedProductsSlider" data-bs-slide-href="0" class="active" aria-current="true" aria-label="Slide 1">
                        </button>
                        <button type="button" data-bs-target="#relatedProductsSlider" data-bs-slide-href="1"  aria-label="Slide 2">
                        </button>
                        <button type="button" data-bs-target="#relatedProductsSlider" data-bs-slide-href="2"  aria-label="Slide 3">
                        </button>

                    </div>
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <div class="row mb-5">

                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="row mb-5">

                        </div>
                    </div>
                    <div class="carousel-item">
                        <div class="row mb-5">

                        </div>
                    </div>
                </div>
                    {/* <button class="carousel-control-prev" type="button" data-bs-target="#relatedProductsSlider" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#relatedProductsSlider" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button> */}
                </div>

            {/* Related Products End */}
        </section>
