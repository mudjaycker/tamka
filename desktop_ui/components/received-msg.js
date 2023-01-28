let received_msg = /*html*/`
              <div class="msg received-msg">
                <p>{{name}}</p>
              </div>
`
function set_msg() {
    return "Yeah"
  }
eel.expose(set_msg)

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