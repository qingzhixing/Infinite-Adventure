// Log service

#include<string>

using std::string;

// Log类主类，其他Log类派生自该类
class Log {
private:
	Log();
	virtual ~Log();
	Log(const Log&) = delete;
	Log& operator=(const Log&) = delete;

public:
	static Log& getInstance();

	// 这个方法用于直接打印类似于 -> [INFO] xx-xx-xx xx:xx:xx 信息...
	virtual void info(string&);
	// 这个方法用于带格式化的打印，如 infof("aaa %s%d", "bbb", 13)
	virtual void infof(string&, ...);

	// 这个方法用于直接打印类似于 -> [DEBUG] xx-xx-xx xx:xx:xx 信息...
	virtual void debug(string&);
	virtual void debugf(string&, ...);

	// 同上
	virtual void error(string&);
	virtual void errorf(string&, ...);
};