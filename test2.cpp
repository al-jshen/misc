#include <dlapi.h>
#include <iostream>
int main()
{
    dl::IGatewayPtr pGateway = dl::getGateway();
    // Query USB Cameras is a blocking call
    pGateway->queryUSBCameras();
    // Only proceed if a camera was found
    if (pGateway->getUSBCameraCount() <= 0)
        return 1;
    // Obtain the first USB camera found
    dl::ICameraPtr pCamera = pGateway->getUSBCamera(0);
    // Initialize the camera (required to enable I/O)
    pCamera->initialize();
    // Create a buffer for the camera's serial string &amp; retrieve it.
    char buf[512] = {0};
    size_t lng = 512;
    pCamera->getSerial(&(buf[0]), lng);
    std::cout << std::string(&(buf[0]), lng) << std::endl;
    
    dl::deleteGateway(pGateway);
    return 0;
}
