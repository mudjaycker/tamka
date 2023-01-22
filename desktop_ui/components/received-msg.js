received_msg = /*html*/`
              <div class="msg received-msg">
                <p>{{name}}</p>
              </div>
`


Vue.component('received-msg', {
    data() {
      return {
        name: "Test"
      }
    },
    template: received_msg,
    props: ["msg"],
    methods: {
      
    },
  })