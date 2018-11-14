using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class Screenshot : MonoBehaviour {
	
	static int i = 0;
	static int j = 0;
	static int sqrtmax = 20;
	//カメラの距離。ポケモンごとに違うので要設定！！！！！
	static int r = 4;
	static Vector3 init = new Vector3(0,1,0);
	static double theta,phi;
	static double x,y,z;
	IEnumerator capture(){
		while(i<sqrtmax){
			j = 0;
			while(j<sqrtmax){
				theta = (180/(sqrtmax-1))*i;
				phi = (360/(sqrtmax-1))*j;
				x = init.x + r * Math.Sin(theta*(Math.PI/180)) * Math.Cos(phi*(Math.PI/180));
				y = init.y + r * Math.Sin(theta*(Math.PI/180)) * Math.Sin(phi*(Math.PI/180));
				z = init.z + r * Math.Cos(theta*(Math.PI/180));
				GetComponent<Camera>().transform.position = new Vector3((float)x,(float)y,(float)z);
				GetComponent<Camera>().transform.LookAt(init);
				Debug.Log("i:"+i+", "+"j:"+j);
				ScreenCapture.CaptureScreenshot("D:/github(bana-titech)/image-deeplearning/deeplearning/teacher/2-all/"+i+"-"+j+"-screenshot.png");
				yield return new WaitForSeconds(1);
				j++;
			}
			i++;
		}
	}
	// Use this for initialization
	void Start () {
		StartCoroutine("capture");
	}
	// Update is called once per frame
	void Update () {
	}
}
