#include"log.h"

// µ¥ÀýÄ£Ê½
Log& Log::getInstance() {
	static Log instance;
	return instance;
}