// Log service

#include<string>

using std::string;

// Log�����࣬����Log�������Ը���
class Log {
private:
	Log();
	virtual ~Log();
	Log(const Log&) = delete;
	Log& operator=(const Log&) = delete;

public:
	static Log& getInstance();

	// �����������ֱ�Ӵ�ӡ������ -> [INFO] xx-xx-xx xx:xx:xx ��Ϣ...
	virtual void info(string&);
	// ����������ڴ���ʽ���Ĵ�ӡ���� infof("aaa %s%d", "bbb", 13)
	virtual void infof(string&, ...);

	// �����������ֱ�Ӵ�ӡ������ -> [DEBUG] xx-xx-xx xx:xx:xx ��Ϣ...
	virtual void debug(string&);
	virtual void debugf(string&, ...);

	// ͬ��
	virtual void error(string&);
	virtual void errorf(string&, ...);
};