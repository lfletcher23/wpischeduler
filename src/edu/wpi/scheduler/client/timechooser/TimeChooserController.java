package edu.wpi.scheduler.client.timechooser;

import edu.wpi.scheduler.client.controller.StudentChosenTimes;
import edu.wpi.scheduler.client.timechooser.TimeChooser;

public class TimeChooserController 
{
	
	TimeChooser view;
	TimeTable view2;
	StudentChosenTimes model;
	
	TimeChooserController(TimeChooser v, StudentChosenTimes model)
	{
		this.view = v;
		this.model = model;
	}

	public TimeChooserController(TimeTable v, StudentChosenTimes model) 
	{
		this.view2 = v;
		this.model = model;
	}

	void timeChosen(double dragX, double dragY, double dropX, double dropY)
	{
		if(dragX > 0 && dragY > 0 && dropX > 0 && dropY > 0)
		{
			// Calculate grid points
			int i1 = (int) Math.floor((Math.min(dragY, dropY)/view.height) * view.numRows);
			int j1 = (int) Math.floor((Math.min(dragX, dropX)/view.width) * view.numColumns);
			int i2 = (int) Math.ceil((Math.max(dragY, dropY)/view.height) * view.numRows);
			int j2 = (int) Math.ceil((Math.max(dragX, dropX)/view.width) * view.numColumns);
			// Update Model
			boolean isSelected = isSelected(dragX, dragY);
			if(isSelected)
			{
				for( int i = i1; i < i2; i++){
					for( int j = j1; j < j2; j++){
						model.deselectTime(i, j);
					}
				}
			}
			else
			{
				for( int i = i1; i < i2; i++){
					for( int j = j1; j < j2; j++){
						model.selectTime(i, j);
					}
				}
			}
			// Update View
			view2.update();
		}
	}
	
	void mouseDrag(double dragX, double dragY, double dropX, double dropY)
	{
		if(dragX > 0 && dragY > 0 && dropX > 0 && dropY > 0)
		{
			// Calculate grid points
			boolean isSelected = isSelected(dragX, dragY);
			int i1 = (int) Math.min(dragY, dropY);
			int j1 = (int) Math.min(dragX, dropX);
			int i2 = (int) Math.max(dragY, dropY);
			int j2 = (int) Math.max(dragX, dropX);
			// Update View
			view2.update();
			//view2.drawDrag(i1, j1, i2, j2, isSelected);
		}
	}
	
	void mouseOut()
	{
		// Update View
		view.redraw();
	}
	
	private boolean isSelected(double dragX, double dragY)
	{
		/*int i = (int) Math.floor((dragY/view.height) * view.numRows);
		int j = (int) Math.floor((dragX/view.width) * view.numColumns);
		return model.isTimeSelected(i, j);*/
		return false;
	}
}