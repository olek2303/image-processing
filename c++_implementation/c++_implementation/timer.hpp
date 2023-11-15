#ifndef TIMER_HPP
#define TIMER_HPP
#include <chrono>
#include <iostream>
using namespace std;
using namespace chrono;

class Timer {
private:
	high_resolution_clock::time_point _start;
	high_resolution_clock::time_point _end;
public:
	Timer() : _start(high_resolution_clock::now()), _end(high_resolution_clock::now()) {};
	void start() {
		_start = high_resolution_clock::now();
	};
	void stop() {
		_end = high_resolution_clock::now();
		microseconds duration = std::chrono::duration_cast<std::chrono::microseconds>(_end - _start);
		cout << "Time of the operation:  " << duration.count() << " microseconds" << endl;
	};
};
#endif // !TIMER_HPP

