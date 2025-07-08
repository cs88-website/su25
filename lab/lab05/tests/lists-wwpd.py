test = {
  'name': 'Lists',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = [7//3, 5, [4, 0, 1], 2]
          >>> s[0]
          31f02e75f8bef5a0621b68131795447b
          # locked
          >>> s[2]
          a29115912254cca523654bdbcc3a813d
          # locked
          >>> s[-1]
          31f02e75f8bef5a0621b68131795447b
          # locked
          >>> len(s)
          fef77a143fa87e746554afe9ebb16a3d
          # locked
          >>> 4 in s
          ac667055c8e3c84ad7260b0fefa2e007
          # locked
          >>> 4 in s[2]
          4975a2633e94dd9ea1ce929c1df08a3b
          # locked
          >>> s[2] + [3 + 2]
          957995096acdc8af0fe4d06e84b4d267
          # locked
          >>> 5 in s[2]
          ac667055c8e3c84ad7260b0fefa2e007
          # locked
          >>> s[2] * 2
          357617fe014804e88f3b625294276c48
          # locked
          >>> list(range(3, 6))
          64a560a48df30fb585341a84030995f3
          # locked
          >>> range(3, 6)
          074e98428db19b6ba875c4c878574242
          # locked
          >>> r = range(3, 6)
          >>> [r[0], r[2]]
          ca08237a9abd8de976149e29b8f08093
          # locked
          >>> range(4)[-1]
          74689fcda5421388b764b40ec8de8ccd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
