const app = Vue.createApp({
    // data, functions
    // template: '<h2>Google</h2>'
    data() {
        return {
            Books: true,
            title: 'Facebook',
            author: 'Flodo',
            age: 25
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
        handleEvent() {
            console.log('event')
        }
    }
})

app.mount('#app')