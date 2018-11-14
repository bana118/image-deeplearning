using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using System;

public class Screenshot : MonoBehaviour {

	// Use this for initialization
	void Start () {
		ScreenCapture.CaptureScreenshot("test.png");
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
