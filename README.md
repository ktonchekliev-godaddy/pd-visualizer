# Incident Visualizer for PaderDuty

---

Tool for displaying triggered and acknowledged incidents assigned to you from [PagerDuty](https://www.pagerduty.com/). <br>
**Note: Currently works only on MacOS due to the package limitations**

### Usage and setup:
1. Create a json file containing your PaderDuty user_id and [API Access Key](https://support.pagerduty.com/docs/api-access-keys), example:
```json
{
  "userId" : "######",
  "apiToken" : "######"
}
```
The `userId` and `apiToken` fields needs to be named the exact same way.
2. Install the required packages
```python
python -m pip install -r requirements.txt 
```
3. Update the script with the path of your config file, this is done with the `configLocation` variable on line 8
4. Run the script in the terminal to confirm everything is working as expected, this will throw any errors if it finds such
5. Setup the script to run on boot, you can use the following stackoverflow article -> [link](https://stackoverflow.com/questions/6442364/running-script-upon-login-in-mac-os-x)

---
### Additional information
You can change how freqent the script to check for new incidents by updating the time in the `pollingTime` variable on line 9, it isn't advised to change it too frequent since it can start usning more resources in the background.
