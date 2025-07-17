#!/usr/bin/env python3
"""
Script to merge both assignment PDFs into a single document
"""

import PyPDF2
import sys

def merge_pdfs():
    # Create a PDF merger object
    merger = PyPDF2.PdfMerger()
    
    try:
        # Add both PDF files to the merger
        print("Adding SF Salaries Exercise...")
        merger.append("01-SF Salaries Exercise.pdf")
        
        print("Adding Ecommerce Purchases Exercise...")
        merger.append("03-Ecommerce Purchases Exercise .pdf")
        
        # Write the merged PDF
        output_file = "Assignment-3-Complete-Milav-Dabgar.pdf"
        print(f"Creating combined PDF: {output_file}")
        
        with open(output_file, 'wb') as output:
            merger.write(output)
        
        merger.close()
        print(f"✅ Successfully created: {output_file}")
        
    except Exception as e:
        print(f"❌ Error merging PDFs: {e}")
        sys.exit(1)

if __name__ == "__main__":
    merge_pdfs()
