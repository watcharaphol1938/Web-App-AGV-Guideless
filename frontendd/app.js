const app = Vue.createApp({
    // data, functions
    // template: '<h2>Google</h2>'
    data() {
        return {
            url: 'http://ww.thenetninja.co.uk',
            Books: true,
            // title: 'Facebook',
            // author: 'Flodo',
            // age: 25,
            // x: 0,
            // y: 0
            books: [
                {title: 'the lords', author: 'flodo baggins', image: 'assets/8219db02f6ab686039fa783cce657794.jpg', isFav: true},
                {title: 'the rings', author: 'sammual james', image: 'assets/bed35207824c431950f498b1bddc8a01--tolkien-middle-earth.jpg', isFav: true},
                {title: 'the mordor', author: 'gandaft', image: 'assets/R.jpg', isFav: false},
            ]
        }
    },
    methods: {
        // changeTitle(title) {
        //     // console.log('click me')
        //     // this.title = 'The lords'
        //     this.title = title
        // }
        toggleShow() {
            // this.show = false
            this.Books = !this.Books
        },
        handleEvent(e, data) {
            // console.log('event')
            console.log(e, e.type)
            if (data)
            {
                console.log(data)
            }
        },
        handleMouseMove(e) {
            this.x = e.offsetX
            this.y = e.offsetY
        },
        toggleFav(book) {
            book.isFav = !book.isFav
        }
    },
    computed: {
        filteredBooks() {
            // return 'google'
            return this.books.filter((books) => books.isFav)
        }
    }
})

app.mount('#app')