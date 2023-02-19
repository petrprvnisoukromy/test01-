while True:
    stream = io.BytesIO()
    camera.capture(stream, format='jpeg')
    data = np.frombuffer(stream.getvalue(), dtype=np.uint8)
    image = cv2.imdecode(data, 1)

    # apply contrast stretch
    contrasted = contrast_stretch(image)

    # save the image
    cv2.imwrite("image_%s.jpg" % counter, contrasted)
    
    time.sleep(2)
    counter += 1
    if counter == 5:
       break