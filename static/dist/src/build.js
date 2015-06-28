(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({"/Users/czapla/testing/react-test/src/js/app.js":[function(require,module,exports){
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

},{}]},{},["/Users/czapla/testing/react-test/src/js/app.js"])
//# sourceMappingURL=data:application/json;charset:utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIm5vZGVfbW9kdWxlcy9icm93c2VyaWZ5L25vZGVfbW9kdWxlcy9icm93c2VyLXBhY2svX3ByZWx1ZGUuanMiLCIvVXNlcnMvY3phcGxhL3Rlc3RpbmcvcmVhY3QtdGVzdC9zcmMvanMvYXBwLmpzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBO0FDQUEsQ0FBQyxDQUFDLFFBQVEsQ0FBQyxDQUFDLEtBQUssQ0FBQyxXQUFXOztFQUUzQixDQUFDLENBQUMsV0FBVyxDQUFDLENBQUMsRUFBRSxDQUFDLE9BQU8sRUFBRSxVQUFVLENBQUMsRUFBRTtJQUN0QyxDQUFDLENBQUMsZUFBZSxDQUFDLENBQUMsT0FBTyxDQUFDLFFBQVEsQ0FBQyxDQUFDO0FBQ3pDLEdBQUcsQ0FBQyxDQUFDOztFQUVILENBQUMsQ0FBQyxXQUFXLENBQUMsQ0FBQyxLQUFLLENBQUMsWUFBWTtJQUMvQixDQUFDLENBQUMsSUFBSSxDQUFDLENBQUMsSUFBSSxDQUFDLFVBQVUsQ0FBQyxDQUFDLEdBQUcsQ0FBQyxZQUFZLEVBQUUsU0FBUyxDQUFDLENBQUM7R0FDdkQsRUFBRSxXQUFXO0lBQ1osQ0FBQyxDQUFDLElBQUksQ0FBQyxDQUFDLElBQUksQ0FBQyxVQUFVLENBQUMsQ0FBQyxHQUFHLENBQUMsWUFBWSxFQUFFLFFBQVEsQ0FBQyxDQUFDO0FBQ3pELEdBQUcsQ0FBQyxDQUFDOztFQUVILENBQUMsQ0FBQyxVQUFVLENBQUMsQ0FBQyxNQUFNLEVBQUUsQ0FBQyxFQUFFLENBQUMsT0FBTyxFQUFFLFVBQVUsQ0FBQyxFQUFFO0lBQzlDLENBQUMsQ0FBQyxXQUFXLENBQUMsQ0FBQyxLQUFLLENBQUMsTUFBTSxDQUFDLENBQUM7QUFDakMsR0FBRyxDQUFDLENBQUM7O0FBRUwsQ0FBQyxDQUFDLENBQUM7QUFDSDs7QUFFQSwrQkFBK0I7O0FBRS9CLGtDQUFrQztBQUNsQyxrQ0FBa0M7QUFDbEMsa0NBQWtDO0FBQ2xDLE9BQU87QUFDUCx1QkFBdUI7QUFDdkIsc0VBQXNFO0FBQ3RFLE9BQU87QUFDUCxvQ0FBb0M7QUFDcEMsb0RBQW9EO0FBQ3BELE9BQU87QUFDUCx1Q0FBdUM7QUFDdkMsb0NBQW9DO0FBQ3BDLE9BQU87QUFDUCx5QkFBeUI7QUFDekIsZUFBZTtBQUNmLCtCQUErQjtBQUMvQix1REFBdUQ7QUFDdkQsZUFBZTtBQUNmLFNBQVM7QUFDVCxNQUFNO0FBQ04sTUFBTTs7QUFFTiwrREFBK0Q7QUFDL0Q7O0FBRUEsaUNBQWlDO0FBQ2pDLHlCQUF5QjtBQUN6QixlQUFlO0FBQ2YsK0JBQStCO0FBQy9CLHFDQUFxQztBQUNyQyw0REFBNEQ7QUFDNUQsaUJBQWlCO0FBQ2pCLGVBQWU7QUFDZixXQUFXO0FBQ1gsTUFBTTtBQUNOLE1BQU07O0FBRU4sOERBQThEO0FBQzlEOztBQUVBLHVDQUF1QztBQUN2Qyx5QkFBeUI7QUFDekIsZUFBZTtBQUNmLFlBQVk7QUFDWixxRUFBcUU7QUFDckUsaURBQWlEO0FBQ2pELGFBQWE7QUFDYixTQUFTO0FBQ1QsTUFBTTtBQUNOLE1BQU07O0FBRU4sMkJBQTJCO0FBQzNCLGtCQUFrQjtBQUNsQix3Q0FBd0M7QUFDeEMseUNBQXlDO0FBQ3pDLE9BQU87QUFDUCxXQUFXIiwiZmlsZSI6ImdlbmVyYXRlZC5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzQ29udGVudCI6WyIoZnVuY3Rpb24gZSh0LG4scil7ZnVuY3Rpb24gcyhvLHUpe2lmKCFuW29dKXtpZighdFtvXSl7dmFyIGE9dHlwZW9mIHJlcXVpcmU9PVwiZnVuY3Rpb25cIiYmcmVxdWlyZTtpZighdSYmYSlyZXR1cm4gYShvLCEwKTtpZihpKXJldHVybiBpKG8sITApO3ZhciBmPW5ldyBFcnJvcihcIkNhbm5vdCBmaW5kIG1vZHVsZSAnXCIrbytcIidcIik7dGhyb3cgZi5jb2RlPVwiTU9EVUxFX05PVF9GT1VORFwiLGZ9dmFyIGw9bltvXT17ZXhwb3J0czp7fX07dFtvXVswXS5jYWxsKGwuZXhwb3J0cyxmdW5jdGlvbihlKXt2YXIgbj10W29dWzFdW2VdO3JldHVybiBzKG4/bjplKX0sbCxsLmV4cG9ydHMsZSx0LG4scil9cmV0dXJuIG5bb10uZXhwb3J0c312YXIgaT10eXBlb2YgcmVxdWlyZT09XCJmdW5jdGlvblwiJiZyZXF1aXJlO2Zvcih2YXIgbz0wO288ci5sZW5ndGg7bysrKXMocltvXSk7cmV0dXJuIHN9KSIsIiQoZG9jdW1lbnQpLnJlYWR5KGZ1bmN0aW9uKCkge1xuXG4gICQoJy5zbGlkZWJhcicpLm9uKFwiY2xpY2tcIiwgZnVuY3Rpb24gKGUpIHtcbiAgICAkKCcubGVmdC5zaWRlYmFyJykuc2lkZWJhcigndG9nZ2xlJyk7XG4gIH0pO1xuXG4gICQoJy5ib29rbWFyaycpLmhvdmVyKGZ1bmN0aW9uICgpIHtcbiAgICAkKHRoaXMpLmZpbmQoJy5pY29uYmFyJykuY3NzKCd2aXNpYmlsaXR5JywgJ3Zpc2libGUnKTtcbiAgfSwgZnVuY3Rpb24oKSB7XG4gICAgJCh0aGlzKS5maW5kKCcuaWNvbmJhcicpLmNzcygndmlzaWJpbGl0eScsICdoaWRkZW4nKTtcbiAgfSk7XG5cbiAgJCgnLm9wdGlvbnMnKS5wYXJlbnQoKS5vbignY2xpY2snLCBmdW5jdGlvbiAoZSkge1xuICAgICQoJy51aS5tb2RhbCcpLm1vZGFsKCdzaG93Jyk7XG4gIH0pO1xuXG59KTtcblxuXG4vLyB2YXIgUmVhY3QgPSByZXF1aXJlKCdyZWFjdCcpXG5cbi8vIHZhciBUaW1lciA9IFJlYWN0LmNyZWF0ZUNsYXNzKHtcbi8vICAgZ2V0SW5pdGlhbFN0YXRlOiBmdW5jdGlvbigpIHtcbi8vICAgICByZXR1cm4ge3NlY29uZHNFbGFwc2VkOiAwfTtcbi8vICAgfSxcbi8vICAgdGljazogZnVuY3Rpb24oKSB7XG4vLyAgICAgdGhpcy5zZXRTdGF0ZSh7c2Vjb25kc0VsYXBzZWQ6IHRoaXMuc3RhdGUuc2Vjb25kc0VsYXBzZWQgKyAxfSk7XG4vLyAgIH0sXG4vLyAgIGNvbXBvbmVudERpZE1vdW50OiBmdW5jdGlvbigpIHtcbi8vICAgICB0aGlzLmludGVydmFsID0gc2V0SW50ZXJ2YWwodGhpcy50aWNrLCAxMDAwKTtcbi8vICAgfSxcbi8vICAgY29tcG9uZW50V2lsbFVubW91bnQ6IGZ1bmN0aW9uKCkge1xuLy8gICAgIGNsZWFySW50ZXJ2YWwodGhpcy5pbnRlcnZhbCk7XG4vLyAgIH0sXG4vLyAgIHJlbmRlcjogZnVuY3Rpb24oKSB7XG4vLyAgICAgcmV0dXJuIChcbi8vICAgICAgIDxkaXYgY2xhc3NOYW1lPVwid2VsbFwiPlxuLy8gICAgICAgICBTZWNvbmRzIEVsYXBzZWQ6IHt0aGlzLnN0YXRlLnNlY29uZHNFbGFwc2VkfVxuLy8gICAgICAgPC9kaXY+XG4vLyAgICAgKTtcbi8vICAgfVxuLy8gfSk7XG5cbi8vIFJlYWN0LnJlbmRlcig8VGltZXIgLz4sIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdjb250ZW50JykpO1xuXG5cbi8vIHZhciBJdGVtID0gUmVhY3QuY3JlYXRlQ2xhc3Moe1xuLy8gICByZW5kZXI6IGZ1bmN0aW9uKCkge1xuLy8gICAgIHJldHVybiAoXG4vLyAgICAgICA8ZGl2IGNsYXNzTmFtZT1cIml0ZW1cIj5cbi8vICAgICAgICAgPGRpdiBjbGFzc05hbWU9XCJ1aSBpbnB1dFwiPlxuLy8gICAgICAgICAgICAgPGlucHV0IHR5cGU9XCJ0ZXh0XCIgcGxhY2Vob2xkZXI9XCJTZWFyY2guLi5cIiAvPlxuLy8gICAgICAgICA8L2Rpdj5cbi8vICAgICAgIDwvZGl2PlxuLy8gICAgICAgKTtcbi8vICAgfVxuLy8gfSk7XG5cbi8vIFJlYWN0LnJlbmRlcig8SXRlbSAvPiwgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2NvbnRlbnQnKSk7XG5cblxuLy8gdmFyIEhlbGxvV29ybGQgPSBSZWFjdC5jcmVhdGVDbGFzcyh7XG4vLyAgIHJlbmRlcjogZnVuY3Rpb24oKSB7XG4vLyAgICAgcmV0dXJuIChcbi8vICAgICAgIDxwPlxuLy8gICAgICAgICBIZWxsbywgPGlucHV0IHR5cGU9XCJ0ZXh0XCIgcGxhY2Vob2xkZXI9XCJZb3VyIG5hbWUgaGVyZVwiIC8+IVxuLy8gICAgICAgICBJdCBpcyB7dGhpcy5wcm9wcy5kYXRlLnRvVGltZVN0cmluZygpfVxuLy8gICAgICAgPC9wPlxuLy8gICAgICk7XG4vLyAgIH1cbi8vIH0pO1xuXG4vLyBzZXRJbnRlcnZhbChmdW5jdGlvbigpIHtcbi8vICAgUmVhY3QucmVuZGVyKFxuLy8gICAgIDxIZWxsb1dvcmxkIGRhdGU9e25ldyBEYXRlKCl9IC8+LFxuLy8gICAgIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdleGFtcGxlJylcbi8vICAgKTtcbi8vIH0sIDUwMCk7XG4iXX0=
