#include"log.h"

// ����ģʽ
Log& Log::getInstance() {
	static Log instance;
	return instance;
}