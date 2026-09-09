function plateLoaderMenuControl(s)
while(1)
    switch(menu('Choose command','Reset','X-Axis',...
            'Z-Axis','Gripper','Move','Status','Special Moves','Exit'))
        case 1
            writeline(s, "RESET")
        case 2
            writeline(s,['X-AXIS ',num2str(menu('Choose location to move to','1','2','3','4','5'))]);
        case 3
            switch(menu('Z-AXIS:','EXTEND','RETRACT'))
                case 1
                    writeline(s,'Z-AXIS EXTEND');
                case 2
                    writeline(s,'Z-AXIS RETRACT');
            end
        case 4
            switch(menu('GRIPPER:', 'OPEN', 'CLOSE'))
                case 1
                    writeline(s, 'GRIPPER OPEN')
                case 2
                    writeline(s, 'GRIPPER CLOSE')
            end
        case 5
            a = menu('Choose location to grab to','1','2','3','4','5');
            b = menu('Choose location to drop to','1','2','3','4','5');
            writeline(s,['MOVE ', num2str(a), ' ', num2str(b)]);
        case 6
            writeline(s, "LOADER_STATUS")
        case 7
            switch(menu('Specal Moves:', 'DANCE', 'Something'))
                case 1
                    uiwait(helpdlg('Please place a plate at location 1'))

                    writeline(s, 'RESET')
                    pause(3)
                    writeline(s, 'X-Axis 1')
                    pause(3)
                    writeline(s, 'GRIPPER OPEN')
                    pause(1.5)
                    writeline(s, 'Z-AXIS EXTEND')
                    pause(1.5)
                    writeline(s, 'GRIPPER CLOSE')
                    pause(1.5)
                    writeline(s, 'GRIPPER OPEN')
                    pause(1.5)
                    writeline(s, 'GRIPPER CLOSE')
                    pause(1.5)
                    writeline(s, 'Z-AXIS RETRACT')
                    pause(1.5)
                    writeline(s, 'X-AXIS 5')
                    pause(3)
                    writeline(s, 'X-AXIS 1')
                    pause(3)
                    writeline(s, 'Z-AXIS EXTEND')
                    pause(1.5)
                    writeline(s, 'GRIPPER CLOSE')
                    pause(1.5)
                    writeline(s, 'GRIPPER OPEN')
                    pause(1.5)
                    writeline(s, 'GRIPPER CLOSE')
                    pause(1.5)
                    writeline(s, 'Z-AXIS RETRACT')
                    pause(1.5)
                    writeline(s, 'X-AXIS 3')
                    pause(3)
                    writeline(s, 'GRIPPER OPEN')
                case 2
                    writeline(s, 'RESET')
            end
        case 8
            fprintf("Goodbye!\n");
            break
    end
    
    readline(s)
end
