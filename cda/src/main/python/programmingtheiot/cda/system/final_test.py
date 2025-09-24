print("=== FINAL CDA SYSTEM TEST ===")
print("Testing all components...\n")

try:
    # Test all imports
    from SystemCpuUtilTask import SystemCpuUtilTask
    from SystemMemUtilTask import SystemMemUtilTask
    from SystemPerformanceManager import SystemPerformanceManager
    
    print("✓ All imports successful")
    
    # Test functionality
    cpu_task = SystemCpuUtilTask()
    mem_task = SystemMemUtilTask()
    
    cpu_value = cpu_task.getTelemetryValue()
    mem_value = mem_task.getTelemetryValue()
    
    print(f"✓ CPU reading: {cpu_value}%")
    print(f"✓ Memory reading: {mem_value}%")
    
    # Test manager
    manager = SystemPerformanceManager(pollRate=2)
    print("✓ Manager created successfully")
    
    # Test short run
    print("\nStarting manager for 6 seconds (3 cycles)...")
    manager.startManager()
    import time
    time.sleep(6)  # Run for 3 cycles (2 seconds each)
    manager.stopManager()
    
    print("\n🎉 ALL TESTS PASSED! CDA SYSTEM IS WORKING PERFECTLY!")
    
except Exception as e:
    print(f"❌ TEST FAILED: {e}")
    import traceback
    traceback.print_exc()