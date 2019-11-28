{
	"targets": [
		{
			"target_name": "xmrigCpu",
			"include_dirs": [
				"src",
				"<!(node -e \"require('nan')\")",
				"src/3rdparty",
				"src/3rdparty/libcpuid"
			],
			"sources": [
				"src/xmrig.cpp",
				"src/NodeXmrigCpu.cpp",
				"src/api/NetworkState.cpp",
				"src/NodeApp.cpp",
				"src/common/config/CommonConfig.cpp",
				"src/common/config/ConfigLoader.cpp",
				"src/common/config/ConfigWatcher.cpp",
				"src/common/Console.cpp",
				"src/common/crypto/Algorithm.cpp",
				"src/common/crypto/keccak.cpp",
				"src/common/log/ConsoleLog.cpp",
				"src/common/log/FileLog.cpp",
				"src/common/log/Log.cpp",
				"src/common/net/Client.cpp",
				"src/common/net/Job.cpp",
				"src/common/net/Pool.cpp",
				"src/common/net/strategies/FailoverStrategy.cpp",
				"src/common/net/strategies/SinglePoolStrategy.cpp",
				"src/common/net/SubmitResult.cpp",
				"src/common/Platform.cpp",
				"src/core/Config.cpp",
				"src/core/Controller.cpp",
				"src/Mem.cpp",
				"src/net/Network.cpp",
				"src/net/strategies/DonateStrategy.cpp",
				"src/Summary.cpp",
				"src/workers/CpuThread.cpp",
				"src/workers/Handle.cpp",
				"src/workers/Hashrate.cpp",
				"src/workers/MultiWorker.cpp",
				"src/workers/Worker.cpp",
				"src/workers/Workers.cpp",
				"src/Cpu.cpp",
				"src/xmrig.cpp",
				"src/crypto/c_groestl.c",
				"src/crypto/c_blake256.c",
				"src/crypto/c_jh.c",
				"src/crypto/c_skein.c",
				"src/3rdparty/libcpuid/asm-bits.c",
				"src/3rdparty/libcpuid/recog_amd.c",
				"src/3rdparty/libcpuid/recog_intel.c",
				"src/3rdparty/libcpuid/libcpuid_util.c",
				"src/3rdparty/libcpuid/cpuid_main.c"
			],
			'cflags!': [
				'-pthread'
			],
			'cflags': [
				"-maes"
			],
			'cflags_cc!': [
				'-std=gnu++0x'
			],
			"cflags_cc": [
				"-std=c++11",
				"-maes",
				"-Wno-unused-variable"
			],
			'defines': [
				'UNICODE',
				'RAPIDJSON_SSE2',
				'XMRIG_NO_HTTPD',
				'XMRIG_NO_API',
				'_GNU_SOURCE'
			],
			'conditions': [
				[
					'OS=="win"',
					{
						'sources': [
							'res/app.rc',
							'src/App_win.cpp',
							'src/common/Platform_win.cpp',
							'src/Cpu_win.cpp',
							'src/Mem_win.cpp',
							'src/3rdparty/libcpuid/masm-x64.asm'
						],
						"defines": [
							"WIN32"
						],
						"link_settings": {
							"libraries": [
								"-lws2_32",
								"-lpsapi",
								"-liphlpapi",
								"-luserenv"
							]
						}
					},
					'OS=="mac"',
					{
						'sources': [
							'src/App_unix.cpp',
							'src/common/Platform_mac.cpp',
							'src/Cpu_mac.cpp',
							'src/Mem_unix.cpp'
						],
						'xcode_settings':
						{
							'OTHER_CFLAGS': ['-maes']
						}

					},
					'OS=="linux"',
					{
						'sources': [
							'src/App_unix.cpp',
							'src/common/Platform_unix.cpp',
							'src/Cpu_mac.cpp',
							'src/Mem_unix.cpp'
						],
						'defines': [
							'NDEBUG',
							'XMRIG_NO_IPBC',
							'__STDC_FORMAT_MACROS'
						],
						"link_settings": {
							"libraries": [
								"-lrt"
							]
						}
					}
				]
			]
		}
	]
}
