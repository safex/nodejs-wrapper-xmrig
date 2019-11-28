#include <nan.h>
#include <string>
#include "NodeApp.h"

class NodeXmrigCpu : public Nan::ObjectWrap {

public:

  std::string jsonConfig;
  NodeApp *minerApp;

  NodeXmrigCpu(const std::string _jsonConfig) {
    jsonConfig = _jsonConfig;
    minerApp = new NodeApp(jsonConfig);
  }

  static NAN_MODULE_INIT(Init);
  static NAN_METHOD(New);

  static NAN_METHOD(startMining);
  static NAN_METHOD(stopMining);
  static NAN_METHOD(getStatus);
  static NAN_METHOD(reloadConfig);

  static NAN_GETTER(HandleGetters);
  static NAN_SETTER(HandleSetters);

  static Nan::Persistent<v8::FunctionTemplate> constructor;

private:



};