import streamlit as st

st.set_page_config(page_title="Chess Master Pro", layout="wide")

st.markdown("""
    <style>
    .chess-container { display: flex; justify-content: center; margin-top: 20px; }
    iframe { border: none; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.15); }
    </style>
""", unsafe_allow_html=True)

st.title("♟️ Chess Master Pro")
st.caption("Giao diện bàn cờ tự động chạy trực tiếp, bấm vào quân cờ để hiển thị gợi ý nước đi màu xanh lá cây.")

# Mã nguồn HTML tích hợp sẵn bộ thư viện cờ vua tự vận hành độc lập
html_code = """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://cloudflare.com">
    <script src="https://cloudflare.com"></script>
    <script src="https://cloudflare.com"></script>
    <script src="https://cloudflare.com"></script>
    <style>
        body { margin: 0; display: flex; justify-content: center; background-color: #ffffff; font-family: sans-serif; }
        #myBoard { width: 450px; margin: 10px auto; }
        .highlight-hint { box-shadow: inset 0 0 4px 4px #22c55e; border-radius: 50%; }
        .white-1e1d7 { background-color: #f0d9b5; color: #b58863; }
        .black-3c85d { background-color: #b58863; color: #f0d9b5; }
    </style>
</head>
<body>
    <div>
        <div id="myBoard"></div>
        <div style="text-align:center; margin-top:15px; color:#333; font-weight:bold; font-size:18px;" id="status">Lượt đi: Trắng</div>
    </div>

    <script>
        var board = null
        var game = new Chess()
        var $status = $('#status')

        function onDragStart (source, piece, position, orientation) {
          if (game.game_over()) return false
          if ((game.turn() === 'w' && piece.search(/^b/) !== -1) ||
              (game.turn() === 'b' && piece.search(/^w/) !== -1)) {
            return false
          }
        }

        // Kích hoạt tính năng: Bấm chuột trái vào quân cờ hiện nước đi xanh lá cây
        $(document).on('mousedown', '.piece-4a305', function() {
            $('.square-55d63').removeClass('highlight-hint');
            var square = $(this).parent().attr('data-square');
            var moves = game.moves({ square: square, verbose: true });
            if (moves.length === 0) return;
            
            moves.forEach(function(move) {
                $('.square-' + move.to).addClass('highlight-hint');
            });
        });

        function onDrop (source, target) {
          $('.square-55d63').removeClass('highlight-hint');
          var move = game.move({ from: source, to: target, promotion: 'q' })
          if (move === null) return 'snapback'
          updateStatus()
        }

        function onSnapEnd () { board.position(game.fen()) }

        function updateStatus () {
          var status = ''
          var moveColor = 'Trắng'
          if (game.turn() === 'b') moveColor = 'Đen'

          if (game.in_checkmate()) {
            status = 'Trò chơi kết thúc, phe ' + moveColor + ' bị chiếu bí.'
          } else if (game.in_draw()) {
            status = 'Trò chơi kết thúc, kết quả Hòa cờ.'
          } else {
            status = 'Lượt đi: ' + moveColor
            if (game.in_check()) { status += ' (Đang bị chiếu!)' }
          }
          $status.html(status)
        }

        var config = {
          draggable: true,
          position: 'start',
          onDragStart: onDragStart,
          onDrop: onDrop,
          onSnapEnd: onSnapEnd,
          pieceTheme: 'https://chessboardjs.com{piece}.png'
        }
        board = Chessboard('myBoard', config)
        updateStatus()
    </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=550)
