{
  'targets': [
    {
      'target_name': 'libpomelo',
      'type': '<(library)',
      'dependencies': [
        'deps/uv/uv.gyp:libuv',
        'deps/jansson/jansson.gyp:jansson',
      ],
      'include_dirs': [
        './include',
        './deps/uv/include',
        './deps/jansson/src',
      ],
      'cflags:': [
        '-std=c99',
      ],
      'sources': [
        'include/pomelo-private/common.h',
        'include/pomelo-private/internal.h',
        'include/pomelo-private/listener.h',
        'include/pomelo-private/map.h',
        'include/pomelo-private/ngx-queue.h',
        'include/pomelo-private/transport.h',
        'include/pomelo-protobuf/pb-util.h',
        'include/pomelo-protobuf/pb.h',
        'include/pomelo-protocol/message.h',
        'include/pomelo-protocol/package.h',
        'include/pomelo.h',
        'src/client.c',
        'src/common.c',
        'src/listener.c',
        'src/map.c',
        'src/message.c',
        'src/msg-json.c',
        'src/msg-pb.c',
        'src/network.c',
        'src/package.c',
        'src/pb-decode.c',
        'src/pb-encode.c',
        'src/pb-util.c',
        'src/pkg-handshake.c',
        'src/pkg-heartbeat.c',
        'src/transport.c'
      ],
    },

    {
      'target_name': 'client',
      'type': 'executable',
      'dependencies': [
        'libpomelo',
      ],
      'include_dirs': [
        'include/',
        './deps/uv/include',
        './deps/jansson/src',
      ],
      'sources': [
        'test/client.c'
      ]
    }
  ],
}
