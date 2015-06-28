$(document).ready(function() {

  $('.slidebar').on("click", function (e) {
    $('.left.sidebar').sidebar('toggle');
  });

  $('.bookmark').hover(function () {
    $(this).find('.iconbar').css('visibility', 'visible');
  }, function() {
    $(this).find('.iconbar').css('visibility', 'hidden');
  });

  $('.options').parent().on('click', function (e) {
    $('.ui.modal').modal('show');
  });

});


// var React = require('react')

// var Timer = React.createClass({
//   getInitialState: function() {
//     return {secondsElapsed: 0};
//   },
//   tick: function() {
//     this.setState({secondsElapsed: this.state.secondsElapsed + 1});
//   },
//   componentDidMount: function() {
//     this.interval = setInterval(this.tick, 1000);
//   },
//   componentWillUnmount: function() {
//     clearInterval(this.interval);
//   },
//   render: function() {
//     return (
//       <div className="well">
//         Seconds Elapsed: {this.state.secondsElapsed}
//       </div>
//     );
//   }
// });

// React.render(<Timer />, document.getElementById('content'));


// var Item = React.createClass({
//   render: function() {
//     return (
//       <div className="item">
//         <div className="ui input">
//             <input type="text" placeholder="Search..." />
//         </div>
//       </div>
//       );
//   }
// });

// React.render(<Item />, document.getElementById('content'));


// var HelloWorld = React.createClass({
//   render: function() {
//     return (
//       <p>
//         Hello, <input type="text" placeholder="Your name here" />!
//         It is {this.props.date.toTimeString()}
//       </p>
//     );
//   }
// });

// setInterval(function() {
//   React.render(
//     <HelloWorld date={new Date()} />,
//     document.getElementById('example')
//   );
// }, 500);
