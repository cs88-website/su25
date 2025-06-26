test = {
  'name': 'Control',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def xk(c, d):
          ...     if c == 4:
          ...         return 6
          ...     elif d >= 4:
          ...         return 6 + 7 + c
          ...     else:
          ...         return 25
          >>> xk(10, 10)
          d6b9d6c018706d1620882d2b53800673
          # locked
          >>> xk(10, 6)
          d6b9d6c018706d1620882d2b53800673
          # locked
          >>> xk(4, 6)
          13e9492c801fddcd5c1330b411f26ac8
          # locked
          >>> xk(0, 0)
          accf8ae456031aaa8e9713cc08c77c51
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> def how_big(x):
          ...     if x > 10:
          ...         print('huge')
          ...     elif x > 5:
          ...         return 'big'
          ...     if x > 0:
          ...         print('positive')
          ...     else:
          ...         print(0)
          >>> how_big(7)  # Be careful with quotation marks!
          23228d5446286b52eccc81dca9f6fae5
          # locked
          >>> print(how_big(7))  # Be careful with quotation marks!
          6f2ec1f592c49e8d8639d93be290ad16
          # locked
          >>> how_big(12)
          6f90a21255238b44281b57070eb3eb40
          616d71b7934a5ed76429a43a10e05fe0
          # locked
          >>> print(how_big(12))
          6f90a21255238b44281b57070eb3eb40
          616d71b7934a5ed76429a43a10e05fe0
          7b760505602b62a147678e737b04445f
          # locked
          >>> print(how_big(1), how_big(0))
          616d71b7934a5ed76429a43a10e05fe0
          b33f256984c474b4181f5512601c4a70
          7a31baae42b52925c9d68a121f9f701f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> n = 3
          >>> while n >= 0:  # If this loops forever, just type Infinite Loop
          ...     n -= 1
          ...     print(n)
          dcbe12f5edfd80d067e49a65db66d0b1
          cf2e1ad2c681425ba709dfa2ee9bde0f
          b33f256984c474b4181f5512601c4a70
          6b4205ba72f3ab35b0da9ecb25ba19dc
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': True
        },
        {
          'code': r"""
          >>> negative = -12
          >>> while negative: # If this loops forever, just type Infinite Loop
          ...    if negative + 6:
          ...        print(negative)
          ...    negative += 3
          5c0b6cbcec878783ea5d3a8e4483fb0a
          2c97387e035b824fc893ae015c7e9440
          05f187dd56858234b8e34e16863f1f41
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
