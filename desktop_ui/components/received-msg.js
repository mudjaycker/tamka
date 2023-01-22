received_msg = /*html*/`
              <div class="msg received-msg">
                <p>{{msg}}</p>
              </div>
`


Vue.component('received-msg', {
    template: received_msg,
    props: ["msg"]
  })