import pywasm

wasm = pywasm.load("TestMethod.wasm")
print(wasm.execute("run_add_array", [1, 2, 3]))
