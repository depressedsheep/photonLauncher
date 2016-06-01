"""
uses usb1 from libusb1 which apparently works while pyusb does not

link to github
https://github.com/vpelletier/python-libusb1

with not so useful ish documentation but it is sufficient for getting the data we need

currently need to finish the proof of concept

then a parser

then a general library to handle everything


zy
4 apr 2016

"""

# run with sudo
import binascii
import struct
import usb1
context = usb1.USBContext()

#ep 2:0x82 --> 130
#ep 6:0x86 --> 134


#init

wavelengths = [345.71, 345.92, 346.14, 346.35, 346.57, 346.79, 347.0, 347.22, 347.43, 347.65, 347.86, 348.08, 348.29, 348.51, 348.72, 348.94, 349.15, 349.37, 349.59, 349.8, 350.02, 350.23, 350.45, 350.66, 350.88, 351.09, 351.31, 351.52, 351.74, 351.95, 352.17, 352.38, 352.6, 352.81, 353.03, 353.25, 353.46, 353.68, 353.89, 354.11, 354.32, 354.54, 354.75, 354.97, 355.18, 355.4, 355.61, 355.83, 356.04, 356.26, 356.47, 356.69, 356.9, 357.12, 357.33, 357.55, 357.76, 357.98, 358.19, 358.41, 358.62, 358.84, 359.05, 359.27, 359.48, 359.69, 359.91, 360.12, 360.34, 360.55, 360.77, 360.98, 361.2, 361.41, 361.63, 361.84, 362.06, 362.27, 362.49, 362.7, 362.92, 363.13, 363.35, 363.56, 363.77, 363.99, 364.2, 364.42, 364.63, 364.85, 365.06, 365.28, 365.49, 365.71, 365.92, 366.13, 366.35, 366.56, 366.78, 366.99, 367.21, 367.42, 367.64, 367.85, 368.06, 368.28, 368.49, 368.71, 368.92, 369.14, 369.35, 369.56, 369.78, 369.99, 370.21, 370.42, 370.64, 370.85, 371.06, 371.28, 371.49, 371.71, 371.92, 372.14, 372.35, 372.56, 372.78, 372.99, 373.21, 373.42, 373.63, 373.85, 374.06, 374.28, 374.49, 374.7, 374.92, 375.13, 375.35, 375.56, 375.77, 375.99, 376.2, 376.42, 376.63, 376.84, 377.06, 377.27, 377.49, 377.7, 377.91, 378.13, 378.34, 378.56, 378.77, 378.98, 379.2, 379.41, 379.62, 379.84, 380.05, 380.27, 380.48, 380.69, 380.91, 381.12, 381.33, 381.55, 381.76, 381.97, 382.19, 382.4, 382.62, 382.83, 383.04, 383.26, 383.47, 383.68, 383.9, 384.11, 384.32, 384.54, 384.75, 384.96, 385.18, 385.39, 385.6, 385.82, 386.03, 386.25, 386.46, 386.67, 386.89, 387.1, 387.31, 387.53, 387.74, 387.95, 388.17, 388.38, 388.59, 388.81, 389.02, 389.23, 389.44, 389.66, 389.87, 390.08, 390.3, 390.51, 390.72, 390.94, 391.15, 391.36, 391.58, 391.79, 392.0, 392.22, 392.43, 392.64, 392.85, 393.07, 393.28, 393.49, 393.71, 393.92, 394.13, 394.35, 394.56, 394.77, 394.98, 395.2, 395.41, 395.62, 395.84, 396.05, 396.26, 396.47, 396.69, 396.9, 397.11, 397.33, 397.54, 397.75, 397.96, 398.18, 398.39, 398.6, 398.82, 399.03, 399.24, 399.45, 399.67, 399.88, 400.09, 400.3, 400.52, 400.73, 400.94, 401.15, 401.37, 401.58, 401.79, 402.0, 402.22, 402.43, 402.64, 402.85, 403.07, 403.28, 403.49, 403.7, 403.92, 404.13, 404.34, 404.55, 404.77, 404.98, 405.19, 405.4, 405.62, 405.83, 406.04, 406.25, 406.47, 406.68, 406.89, 407.1, 407.31, 407.53, 407.74, 407.95, 408.16, 408.38, 408.59, 408.8, 409.01, 409.22, 409.44, 409.65, 409.86, 410.07, 410.28, 410.5, 410.71, 410.92, 411.13, 411.35, 411.56, 411.77, 411.98, 412.19, 412.41, 412.62, 412.83, 413.04, 413.25, 413.46, 413.68, 413.89, 414.1, 414.31, 414.52, 414.74, 414.95, 415.16, 415.37, 415.58, 415.8, 416.01, 416.22, 416.43, 416.64, 416.85, 417.07, 417.28, 417.49, 417.7, 417.91, 418.12, 418.34, 418.55, 418.76, 418.97, 419.18, 419.39, 419.6, 419.82, 420.03, 420.24, 420.45, 420.66, 420.87, 421.09, 421.3, 421.51, 421.72, 421.93, 422.14, 422.35, 422.57, 422.78, 422.99, 423.2, 423.41, 423.62, 423.83, 424.04, 424.26, 424.47, 424.68, 424.89, 425.1, 425.31, 425.52, 425.74, 425.95, 426.16, 426.37, 426.58, 426.79, 427.0, 427.21, 427.42, 427.64, 427.85, 428.06, 428.27, 428.48, 428.69, 428.9, 429.11, 429.32, 429.53, 429.75, 429.96, 430.17, 430.38, 430.59, 430.8, 431.01, 431.22, 431.43, 431.64, 431.86, 432.07, 432.28, 432.49, 432.7, 432.91, 433.12, 433.33, 433.54, 433.75, 433.96, 434.17, 434.38, 434.6, 434.81, 435.02, 435.23, 435.44, 435.65, 435.86, 436.07, 436.28, 436.49, 436.7, 436.91, 437.12, 437.33, 437.54, 437.75, 437.96, 438.18, 438.39, 438.6, 438.81, 439.02, 439.23, 439.44, 439.65, 439.86, 440.07, 440.28, 440.49, 440.7, 440.91, 441.12, 441.33, 441.54, 441.75, 441.96, 442.17, 442.38, 442.59, 442.8, 443.01, 443.22, 443.43, 443.64, 443.85, 444.06, 444.27, 444.49, 444.7, 444.91, 445.12, 445.33, 445.54, 445.75, 445.96, 446.17, 446.38, 446.59, 446.8, 447.01, 447.22, 447.43, 447.64, 447.85, 448.06, 448.27, 448.48, 448.69, 448.9, 449.11, 449.31, 449.52, 449.73, 449.94, 450.15, 450.36, 450.57, 450.78, 450.99, 451.2, 451.41, 451.62, 451.83, 452.04, 452.25, 452.46, 452.67, 452.88, 453.09, 453.3, 453.51, 453.72, 453.93, 454.14, 454.35, 454.56, 454.77, 454.98, 455.19, 455.4, 455.61, 455.81, 456.02, 456.23, 456.44, 456.65, 456.86, 457.07, 457.28, 457.49, 457.7, 457.91, 458.12, 458.33, 458.54, 458.75, 458.96, 459.16, 459.37, 459.58, 459.79, 460.0, 460.21, 460.42, 460.63, 460.84, 461.05, 461.26, 461.47, 461.68, 461.88, 462.09, 462.3, 462.51, 462.72, 462.93, 463.14, 463.35, 463.56, 463.77, 463.97, 464.18, 464.39, 464.6, 464.81, 465.02, 465.23, 465.44, 465.65, 465.86, 466.06, 466.27, 466.48, 466.69, 466.9, 467.11, 467.32, 467.53, 467.73, 467.94, 468.15, 468.36, 468.57, 468.78, 468.99, 469.2, 469.4, 469.61, 469.82, 470.03, 470.24, 470.45, 470.66, 470.86, 471.07, 471.28, 471.49, 471.7, 471.91, 472.12, 472.32, 472.53, 472.74, 472.95, 473.16, 473.37, 473.58, 473.78, 473.99, 474.2, 474.41, 474.62, 474.83, 475.03, 475.24, 475.45, 475.66, 475.87, 476.08, 476.28, 476.49, 476.7, 476.91, 477.12, 477.32, 477.53, 477.74, 477.95, 478.16, 478.37, 478.57, 478.78, 478.99, 479.2, 479.41, 479.61, 479.82, 480.03, 480.24, 480.45, 480.65, 480.86, 481.07, 481.28, 481.49, 481.69, 481.9, 482.11, 482.32, 482.53, 482.73, 482.94, 483.15, 483.36, 483.57, 483.77, 483.98, 484.19, 484.4, 484.6, 484.81, 485.02, 485.23, 485.44, 485.64, 485.85, 486.06, 486.27, 486.47, 486.68, 486.89, 487.1, 487.3, 487.51, 487.72, 487.93, 488.13, 488.34, 488.55, 488.76, 488.96, 489.17, 489.38, 489.59, 489.79, 490.0, 490.21, 490.42, 490.62, 490.83, 491.04, 491.25, 491.45, 491.66, 491.87, 492.08, 492.28, 492.49, 492.7, 492.9, 493.11, 493.32, 493.53, 493.73, 493.94, 494.15, 494.36, 494.56, 494.77, 494.98, 495.18, 495.39, 495.6, 495.81, 496.01, 496.22, 496.43, 496.63, 496.84, 497.05, 497.25, 497.46, 497.67, 497.88, 498.08, 498.29, 498.5, 498.7, 498.91, 499.12, 499.32, 499.53, 499.74, 499.94, 500.15, 500.36, 500.56, 500.77, 500.98, 501.18, 501.39, 501.6, 501.8, 502.01, 502.22, 502.43, 502.63, 502.84, 503.05, 503.25, 503.46, 503.66, 503.87, 504.08, 504.28, 504.49, 504.7, 504.9, 505.11, 505.32, 505.52, 505.73, 505.94, 506.14, 506.35, 506.56, 506.76, 506.97, 507.18, 507.38, 507.59, 507.79, 508.0, 508.21, 508.41, 508.62, 508.83, 509.03, 509.24, 509.44, 509.65, 509.86, 510.06, 510.27, 510.48, 510.68, 510.89, 511.09, 511.3, 511.51, 511.71, 511.92, 512.12, 512.33, 512.54, 512.74, 512.95, 513.15, 513.36, 513.57, 513.77, 513.98, 514.18, 514.39, 514.6, 514.8, 515.01, 515.21, 515.42, 515.63, 515.83, 516.04, 516.24, 516.45, 516.66, 516.86, 517.07, 517.27, 517.48, 517.68, 517.89, 518.1, 518.3, 518.51, 518.71, 518.92, 519.12, 519.33, 519.53, 519.74, 519.95, 520.15, 520.36, 520.56, 520.77, 520.97, 521.18, 521.38, 521.59, 521.8, 522.0, 522.21, 522.41, 522.62, 522.82, 523.03, 523.23, 523.44, 523.64, 523.85, 524.06, 524.26, 524.47, 524.67, 524.88, 525.08, 525.29, 525.49, 525.7, 525.9, 526.11, 526.31, 526.52, 526.72, 526.93, 527.13, 527.34, 527.54, 527.75, 527.95, 528.16, 528.36, 528.57, 528.77, 528.98, 529.18, 529.39, 529.59, 529.8, 530.0, 530.21, 530.41, 530.62, 530.82, 531.03, 531.23, 531.44, 531.64, 531.85, 532.05, 532.26, 532.46, 532.67, 532.87, 533.08, 533.28, 533.49, 533.69, 533.9, 534.1, 534.31, 534.51, 534.71, 534.92, 535.12, 535.33, 535.53, 535.74, 535.94, 536.15, 536.35, 536.56, 536.76, 536.96, 537.17, 537.37, 537.58, 537.78, 537.99, 538.19, 538.4, 538.6, 538.8, 539.01, 539.21, 539.42, 539.62, 539.83, 540.03, 540.24, 540.44, 540.64, 540.85, 541.05, 541.26, 541.46, 541.66, 541.87, 542.07, 542.28, 542.48, 542.69, 542.89, 543.09, 543.3, 543.5, 543.71, 543.91, 544.11, 544.32, 544.52, 544.73, 544.93, 545.13, 545.34, 545.54, 545.75, 545.95, 546.15, 546.36, 546.56, 546.77, 546.97, 547.17, 547.38, 547.58, 547.78, 547.99, 548.19, 548.4, 548.6, 548.8, 549.01, 549.21, 549.41, 549.62, 549.82, 550.03, 550.23, 550.43, 550.64, 550.84, 551.04, 551.25, 551.45, 551.65, 551.86, 552.06, 552.27, 552.47, 552.67, 552.88, 553.08, 553.28, 553.49, 553.69, 553.89, 554.1, 554.3, 554.5, 554.71, 554.91, 555.11, 555.32, 555.52, 555.72, 555.93, 556.13, 556.33, 556.54, 556.74, 556.94, 557.15, 557.35, 557.55, 557.76, 557.96, 558.16, 558.36, 558.57, 558.77, 558.97, 559.18, 559.38, 559.58, 559.79, 559.99, 560.19, 560.4, 560.6, 560.8, 561.0, 561.21, 561.41, 561.61, 561.82, 562.02, 562.22, 562.42, 562.63, 562.83, 563.03, 563.24, 563.44, 563.64, 563.84, 564.05, 564.25, 564.45, 564.66, 564.86, 565.06, 565.26, 565.47, 565.67, 565.87, 566.07, 566.28, 566.48, 566.68, 566.88, 567.09, 567.29, 567.49, 567.69, 567.9, 568.1, 568.3, 568.5, 568.71, 568.91, 569.11, 569.31, 569.52, 569.72, 569.92, 570.12, 570.33, 570.53, 570.73, 570.93, 571.13, 571.34, 571.54, 571.74, 571.94, 572.15, 572.35, 572.55, 572.75, 572.95, 573.16, 573.36, 573.56, 573.76, 573.97, 574.17, 574.37, 574.57, 574.77, 574.98, 575.18, 575.38, 575.58, 575.78, 575.99, 576.19, 576.39, 576.59, 576.79, 577.0, 577.2, 577.4, 577.6, 577.8, 578.0, 578.21, 578.41, 578.61, 578.81, 579.01, 579.22, 579.42, 579.62, 579.82, 580.02, 580.22, 580.43, 580.63, 580.83, 581.03, 581.23, 581.43, 581.63, 581.84, 582.04, 582.24, 582.44, 582.64, 582.84, 583.05, 583.25, 583.45, 583.65, 583.85, 584.05, 584.25, 584.46, 584.66, 584.86, 585.06, 585.26, 585.46, 585.66, 585.86, 586.07, 586.27, 586.47, 586.67, 586.87, 587.07, 587.27, 587.47, 587.68, 587.88, 588.08, 588.28, 588.48, 588.68, 588.88, 589.08, 589.28, 589.49, 589.69, 589.89, 590.09, 590.29, 590.49, 590.69, 590.89, 591.09, 591.29, 591.5, 591.7, 591.9, 592.1, 592.3, 592.5, 592.7, 592.9, 593.1, 593.3, 593.5, 593.7, 593.91, 594.11, 594.31, 594.51, 594.71, 594.91, 595.11, 595.31, 595.51, 595.71, 595.91, 596.11, 596.31, 596.51, 596.71, 596.92, 597.12, 597.32, 597.52, 597.72, 597.92, 598.12, 598.32, 598.52, 598.72, 598.92, 599.12, 599.32, 599.52, 599.72, 599.92, 600.12, 600.32, 600.52, 600.72, 600.92, 601.12, 601.32, 601.52, 601.72, 601.92, 602.12, 602.32, 602.52, 602.72, 602.93, 603.13, 603.33, 603.53, 603.73, 603.93, 604.13, 604.33, 604.53, 604.73, 604.93, 605.13, 605.33, 605.53, 605.73, 605.93, 606.13, 606.33, 606.53, 606.72, 606.92, 607.12, 607.32, 607.52, 607.72, 607.92, 608.12, 608.32, 608.52, 608.72, 608.92, 609.12, 609.32, 609.52, 609.72, 609.92, 610.12, 610.32, 610.52, 610.72, 610.92, 611.12, 611.32, 611.52, 611.72, 611.92, 612.12, 612.32, 612.52, 612.71, 612.91, 613.11, 613.31, 613.51, 613.71, 613.91, 614.11, 614.31, 614.51, 614.71, 614.91, 615.11, 615.31, 615.51, 615.7, 615.9, 616.1, 616.3, 616.5, 616.7, 616.9, 617.1, 617.3, 617.5, 617.7, 617.9, 618.09, 618.29, 618.49, 618.69, 618.89, 619.09, 619.29, 619.49, 619.69, 619.89, 620.08, 620.28, 620.48, 620.68, 620.88, 621.08, 621.28, 621.48, 621.68, 621.87, 622.07, 622.27, 622.47, 622.67, 622.87, 623.07, 623.27, 623.46, 623.66, 623.86, 624.06, 624.26, 624.46, 624.66, 624.85, 625.05, 625.25, 625.45, 625.65, 625.85, 626.05, 626.24, 626.44, 626.64, 626.84, 627.04, 627.24, 627.44, 627.63, 627.83, 628.03, 628.23, 628.43, 628.63, 628.82, 629.02, 629.22, 629.42, 629.62, 629.82, 630.01, 630.21, 630.41, 630.61, 630.81, 631.0, 631.2, 631.4, 631.6, 631.8, 632.0, 632.19, 632.39, 632.59, 632.79, 632.99, 633.18, 633.38, 633.58, 633.78, 633.98, 634.17, 634.37, 634.57, 634.77, 634.97, 635.16, 635.36, 635.56, 635.76, 635.95, 636.15, 636.35, 636.55, 636.75, 636.94, 637.14, 637.34, 637.54, 637.73, 637.93, 638.13, 638.33, 638.52, 638.72, 638.92, 639.12, 639.32, 639.51, 639.71, 639.91, 640.11, 640.3, 640.5, 640.7, 640.9, 641.09, 641.29, 641.49, 641.68, 641.88, 642.08, 642.28, 642.47, 642.67, 642.87, 643.07, 643.26, 643.46, 643.66, 643.86, 644.05, 644.25, 644.45, 644.64, 644.84, 645.04, 645.24, 645.43, 645.63, 645.83, 646.02, 646.22, 646.42, 646.62, 646.81, 647.01, 647.21, 647.4, 647.6, 647.8, 647.99, 648.19, 648.39, 648.59, 648.78, 648.98, 649.18, 649.37, 649.57, 649.77, 649.96, 650.16, 650.36, 650.55, 650.75, 650.95, 651.14, 651.34, 651.54, 651.73, 651.93, 652.13, 652.32, 652.52, 652.72, 652.91, 653.11, 653.31, 653.5, 653.7, 653.9, 654.09, 654.29, 654.49, 654.68, 654.88, 655.08, 655.27, 655.47, 655.66, 655.86, 656.06, 656.25, 656.45, 656.65, 656.84, 657.04, 657.24, 657.43, 657.63, 657.82, 658.02, 658.22, 658.41, 658.61, 658.8, 659.0, 659.2, 659.39, 659.59, 659.79, 659.98, 660.18, 660.37, 660.57, 660.77, 660.96, 661.16, 661.35, 661.55, 661.75, 661.94, 662.14, 662.33, 662.53, 662.73, 662.92, 663.12, 663.31, 663.51, 663.7, 663.9, 664.1, 664.29, 664.49, 664.68, 664.88, 665.07, 665.27, 665.47, 665.66, 665.86, 666.05, 666.25, 666.44, 666.64, 666.84, 667.03, 667.23, 667.42, 667.62, 667.81, 668.01, 668.2, 668.4, 668.59, 668.79, 668.99, 669.18, 669.38, 669.57, 669.77, 669.96, 670.16, 670.35, 670.55, 670.74, 670.94, 671.13, 671.33, 671.52, 671.72, 671.92, 672.11, 672.31, 672.5, 672.7, 672.89, 673.09, 673.28, 673.48, 673.67, 673.87, 674.06, 674.26, 674.45, 674.65, 674.84, 675.04, 675.23, 675.43, 675.62, 675.82, 676.01, 676.21, 676.4, 676.6, 676.79, 676.99, 677.18, 677.37, 677.57, 677.76, 677.96, 678.15, 678.35, 678.54, 678.74, 678.93, 679.13, 679.32, 679.52, 679.71, 679.91, 680.1, 680.3, 680.49, 680.68, 680.88, 681.07, 681.27, 681.46, 681.66, 681.85, 682.05, 682.24, 682.43, 682.63, 682.82, 683.02, 683.21, 683.41, 683.6, 683.79, 683.99, 684.18, 684.38, 684.57, 684.77, 684.96, 685.15, 685.35, 685.54, 685.74, 685.93, 686.13, 686.32, 686.51, 686.71, 686.9, 687.1, 687.29, 687.48, 687.68, 687.87, 688.07, 688.26, 688.45, 688.65, 688.84, 689.04, 689.23, 689.42, 689.62, 689.81, 690.01, 690.2, 690.39, 690.59, 690.78, 690.97, 691.17, 691.36, 691.56, 691.75, 691.94, 692.14, 692.33, 692.52, 692.72, 692.91, 693.1, 693.3, 693.49, 693.69, 693.88, 694.07, 694.27, 694.46, 694.65, 694.85, 695.04, 695.23, 695.43, 695.62, 695.81, 696.01, 696.2, 696.39, 696.59, 696.78, 696.97, 697.17, 697.36, 697.55, 697.75, 697.94, 698.13, 698.33, 698.52, 698.71, 698.91, 699.1, 699.29, 699.49, 699.68, 699.87, 700.06, 700.26, 700.45, 700.64, 700.84, 701.03, 701.22, 701.42, 701.61, 701.8, 701.99, 702.19, 702.38, 702.57, 702.77, 702.96, 703.15, 703.34, 703.54, 703.73, 703.92, 704.12, 704.31, 704.5, 704.69, 704.89, 705.08, 705.27, 705.46, 705.66, 705.85, 706.04, 706.24, 706.43, 706.62, 706.81, 707.01, 707.2, 707.39, 707.58, 707.78, 707.97, 708.16, 708.35, 708.55, 708.74, 708.93, 709.12, 709.31, 709.51, 709.7, 709.89, 710.08, 710.28, 710.47, 710.66, 710.85, 711.05, 711.24, 711.43, 711.62, 711.81, 712.01, 712.2, 712.39, 712.58, 712.77, 712.97, 713.16, 713.35, 713.54, 713.74, 713.93, 714.12, 714.31, 714.5, 714.7, 714.89, 715.08, 715.27, 715.46, 715.65, 715.85, 716.04, 716.23, 716.42, 716.61, 716.81, 717.0, 717.19, 717.38, 717.57, 717.76, 717.96, 718.15, 718.34, 718.53, 718.72, 718.91, 719.11, 719.3, 719.49, 719.68, 719.87, 720.06, 720.25, 720.45, 720.64, 720.83, 721.02, 721.21, 721.4, 721.6, 721.79, 721.98, 722.17, 722.36, 722.55, 722.74, 722.93, 723.13, 723.32, 723.51, 723.7, 723.89, 724.08, 724.27, 724.46, 724.66, 724.85, 725.04, 725.23, 725.42, 725.61, 725.8, 725.99, 726.18, 726.38, 726.57, 726.76, 726.95, 727.14, 727.33, 727.52, 727.71, 727.9, 728.09, 728.28, 728.48, 728.67, 728.86, 729.05, 729.24, 729.43, 729.62, 729.81, 730.0, 730.19, 730.38, 730.57, 730.76, 730.96, 731.15, 731.34, 731.53, 731.72, 731.91, 732.1, 732.29, 732.48, 732.67, 732.86, 733.05, 733.24, 733.43, 733.62, 733.81, 734.0, 734.19, 734.39, 734.58, 734.77, 734.96, 735.15, 735.34, 735.53, 735.72, 735.91, 736.1, 736.29, 736.48, 736.67, 736.86, 737.05, 737.24, 737.43, 737.62, 737.81, 738.0, 738.19, 738.38, 738.57, 738.76, 738.95, 739.14, 739.33, 739.52, 739.71, 739.9, 740.09, 740.28, 740.47, 740.66, 740.85, 741.04, 741.23, 741.42, 741.61, 741.8, 741.99, 742.18, 742.37, 742.56, 742.75, 742.94, 743.13, 743.32, 743.51, 743.7, 743.89, 744.07, 744.26, 744.45, 744.64, 744.83, 745.02, 745.21, 745.4, 745.59, 745.78, 745.97, 746.16, 746.35, 746.54, 746.73, 746.92, 747.11, 747.3, 747.49, 747.67, 747.86, 748.05, 748.24, 748.43, 748.62, 748.81, 749.0, 749.19, 749.38, 749.57, 749.76, 749.95, 750.13, 750.32, 750.51, 750.7, 750.89, 751.08, 751.27, 751.46, 751.65, 751.84, 752.03, 752.21, 752.4, 752.59, 752.78, 752.97, 753.16, 753.35, 753.54, 753.73, 753.91, 754.1, 754.29, 754.48, 754.67, 754.86, 755.05, 755.24, 755.42, 755.61, 755.8, 755.99, 756.18, 756.37, 756.56, 756.74, 756.93, 757.12, 757.31, 757.5, 757.69, 757.88, 758.06, 758.25, 758.44, 758.63, 758.82, 759.01, 759.19, 759.38, 759.57, 759.76, 759.95, 760.14, 760.32, 760.51, 760.7, 760.89, 761.08, 761.27, 761.45, 761.64, 761.83, 762.02, 762.21, 762.4, 762.58, 762.77, 762.96, 763.15, 763.34, 763.52, 763.71, 763.9, 764.09, 764.28, 764.46, 764.65, 764.84, 765.03, 765.22, 765.4, 765.59, 765.78, 765.97, 766.15, 766.34, 766.53, 766.72, 766.91, 767.09, 767.28, 767.47, 767.66, 767.84, 768.03, 768.22, 768.41, 768.59, 768.78, 768.97, 769.16, 769.34, 769.53, 769.72, 769.91, 770.09, 770.28, 770.47, 770.66, 770.84, 771.03, 771.22, 771.41, 771.59, 771.78, 771.97, 772.16, 772.34, 772.53, 772.72, 772.91, 773.09, 773.28, 773.47, 773.65, 773.84, 774.03, 774.22, 774.4, 774.59, 774.78, 774.96, 775.15, 775.34, 775.53, 775.71, 775.9, 776.09, 776.27, 776.46, 776.65, 776.83, 777.02, 777.21, 777.39, 777.58, 777.77, 777.96, 778.14, 778.33, 778.52, 778.7, 778.89, 779.08, 779.26, 779.45, 779.64, 779.82, 780.01, 780.2, 780.38, 780.57, 780.76, 780.94, 781.13, 781.32, 781.5, 781.69, 781.88, 782.06, 782.25, 782.43, 782.62, 782.81, 782.99, 783.18, 783.37, 783.55, 783.74, 783.93, 784.11, 784.3, 784.48, 784.67, 784.86, 785.04, 785.23, 785.42, 785.6, 785.79, 785.97, 786.16, 786.35, 786.53, 786.72, 786.91, 787.09, 787.28, 787.46, 787.65, 787.84, 788.02, 788.21, 788.39, 788.58, 788.77, 788.95, 789.14, 789.32, 789.51, 789.69, 789.88, 790.07, 790.25, 790.44, 790.62, 790.81, 790.99, 791.18, 791.37, 791.55, 791.74, 791.92, 792.11, 792.29, 792.48, 792.67, 792.85, 793.04, 793.22, 793.41, 793.59, 793.78, 793.96, 794.15, 794.34, 794.52, 794.71, 794.89, 795.08, 795.26, 795.45, 795.63, 795.82, 796.0, 796.19, 796.37, 796.56, 796.74, 796.93, 797.12, 797.3, 797.49, 797.67, 797.86, 798.04, 798.23, 798.41, 798.6, 798.78, 798.97, 799.15, 799.34, 799.52, 799.71, 799.89, 800.08, 800.26, 800.45, 800.63, 800.82, 801.0, 801.19, 801.37, 801.56, 801.74, 801.93, 802.11, 802.29, 802.48, 802.66, 802.85, 803.03, 803.22, 803.4, 803.59, 803.77, 803.96, 804.14, 804.33, 804.51, 804.7, 804.88, 805.06, 805.25, 805.43, 805.62, 805.8, 805.99, 806.17, 806.36, 806.54, 806.72, 806.91, 807.09, 807.28, 807.46, 807.65, 807.83, 808.01, 808.2, 808.38, 808.57, 808.75, 808.94, 809.12, 809.3, 809.49, 809.67, 809.86, 810.04, 810.22, 810.41, 810.59, 810.78, 810.96, 811.14, 811.33, 811.51, 811.7, 811.88, 812.06, 812.25, 812.43, 812.62, 812.8, 812.98, 813.17, 813.35, 813.54, 813.72, 813.9, 814.09, 814.27, 814.45, 814.64, 814.82, 815.01, 815.19, 815.37, 815.56, 815.74, 815.92, 816.11, 816.29, 816.47, 816.66, 816.84, 817.02, 817.21, 817.39, 817.57, 817.76, 817.94, 818.12, 818.31, 818.49, 818.68, 818.86, 819.04, 819.22, 819.41, 819.59, 819.77, 819.96, 820.14, 820.32, 820.51, 820.69, 820.87, 821.06, 821.24, 821.42, 821.61, 821.79, 821.97, 822.16, 822.34, 822.52, 822.7, 822.89, 823.07, 823.25, 823.44, 823.62, 823.8, 823.98, 824.17, 824.35, 824.53, 824.72, 824.9, 825.08, 825.26, 825.45, 825.63, 825.81, 826.0, 826.18, 826.36, 826.54, 826.73, 826.91, 827.09, 827.27, 827.46, 827.64, 827.82, 828.0, 828.19, 828.37, 828.55, 828.73, 828.92, 829.1, 829.28, 829.46, 829.65, 829.83, 830.01, 830.19, 830.38, 830.56, 830.74, 830.92, 831.1, 831.29, 831.47, 831.65, 831.83, 832.02, 832.2, 832.38, 832.56, 832.74, 832.93, 833.11, 833.29, 833.47, 833.65, 833.84, 834.02, 834.2, 834.38, 834.56, 834.75, 834.93, 835.11, 835.29, 835.47, 835.66, 835.84, 836.02, 836.2, 836.38, 836.56, 836.75, 836.93, 837.11, 837.29, 837.47, 837.65, 837.84, 838.02, 838.2, 838.38, 838.56, 838.74, 838.93, 839.11, 839.29, 839.47, 839.65, 839.83, 840.01, 840.2, 840.38, 840.56, 840.74, 840.92, 841.1, 841.28, 841.47, 841.65, 841.83, 842.01, 842.19, 842.37, 842.55, 842.73, 842.92, 843.1, 843.28, 843.46, 843.64, 843.82, 844.0, 844.18, 844.36, 844.55, 844.73, 844.91, 845.09, 845.27, 845.45, 845.63, 845.81, 845.99, 846.17, 846.35, 846.54, 846.72, 846.9, 847.08, 847.26, 847.44, 847.62, 847.8, 847.98, 848.16, 848.34, 848.52, 848.7, 848.89, 849.07, 849.25, 849.43, 849.61, 849.79, 849.97, 850.15, 850.33, 850.51, 850.69, 850.87, 851.05, 851.23, 851.41, 851.59, 851.77, 851.95, 852.13, 852.31, 852.49, 852.67, 852.85, 853.04, 853.22, 853.4, 853.58, 853.76, 853.94, 854.12, 854.3, 854.48, 854.66, 854.84, 855.02, 855.2, 855.38, 855.56, 855.74, 855.92, 856.1, 856.28, 856.46, 856.64, 856.82, 857.0, 857.18, 857.36, 857.54, 857.72, 857.9, 858.08, 858.26, 858.44, 858.62, 858.79, 858.97, 859.15, 859.33, 859.51, 859.69, 859.87, 860.05, 860.23, 860.41, 860.59, 860.77, 860.95, 861.13, 861.31, 861.49, 861.67, 861.85, 862.03, 862.21, 862.39, 862.57, 862.74, 862.92, 863.1, 863.28, 863.46, 863.64, 863.82, 864.0, 864.18, 864.36, 864.54, 864.72, 864.9, 865.08, 865.25, 865.43, 865.61, 865.79, 865.97, 866.15, 866.33, 866.51, 866.69, 866.87, 867.04, 867.22, 867.4, 867.58, 867.76, 867.94, 868.12, 868.3, 868.48, 868.65, 868.83, 869.01, 869.19, 869.37, 869.55, 869.73, 869.91, 870.08, 870.26, 870.44, 870.62, 870.8, 870.98, 871.16, 871.33, 871.51, 871.69, 871.87, 872.05, 872.23, 872.41, 872.58, 872.76, 872.94, 873.12, 873.3, 873.48, 873.65, 873.83, 874.01, 874.19, 874.37, 874.55, 874.72, 874.9, 875.08, 875.26, 875.44, 875.62, 875.79, 875.97, 876.15, 876.33, 876.51, 876.68, 876.86, 877.04, 877.22, 877.4, 877.57, 877.75, 877.93, 878.11, 878.29, 878.46, 878.64, 878.82, 879.0, 879.18, 879.35, 879.53, 879.71, 879.89, 880.06, 880.24, 880.42, 880.6, 880.77, 880.95, 881.13, 881.31, 881.49, 881.66, 881.84, 882.02, 882.2, 882.37, 882.55, 882.73, 882.91, 883.08, 883.26, 883.44, 883.62, 883.79, 883.97, 884.15, 884.32, 884.5, 884.68, 884.86, 885.03, 885.21, 885.39, 885.57, 885.74, 885.92, 886.1, 886.27, 886.45, 886.63, 886.81, 886.98, 887.16, 887.34, 887.51, 887.69, 887.87, 888.05, 888.22, 888.4, 888.58, 888.75, 888.93, 889.11, 889.28, 889.46, 889.64, 889.81, 889.99, 890.17, 890.34, 890.52, 890.7, 890.87, 891.05, 891.23, 891.4, 891.58, 891.76, 891.93, 892.11, 892.29, 892.46, 892.64, 892.82, 892.99, 893.17, 893.35, 893.52, 893.7, 893.88, 894.05, 894.23, 894.41, 894.58, 894.76, 894.93, 895.11, 895.29, 895.46, 895.64, 895.82, 895.99, 896.17, 896.34, 896.52, 896.7, 896.87, 897.05, 897.23, 897.4, 897.58, 897.75, 897.93, 898.11, 898.28, 898.46, 898.63, 898.81, 898.99, 899.16, 899.34, 899.51, 899.69, 899.86, 900.04, 900.22, 900.39, 900.57, 900.74, 900.92, 901.1, 901.27, 901.45, 901.62, 901.8, 901.97, 902.15, 902.32, 902.5, 902.68, 902.85, 903.03, 903.2, 903.38, 903.55, 903.73, 903.9, 904.08, 904.26, 904.43, 904.61, 904.78, 904.96, 905.13, 905.31, 905.48, 905.66, 905.83, 906.01, 906.18, 906.36, 906.53, 906.71, 906.88, 907.06, 907.24, 907.41, 907.59, 907.76, 907.94, 908.11, 908.29, 908.46, 908.64, 908.81, 908.99, 909.16, 909.34, 909.51, 909.69, 909.86, 910.03, 910.21, 910.38, 910.56, 910.73, 910.91, 911.08, 911.26, 911.43, 911.61, 911.78, 911.96, 912.13, 912.31, 912.48, 912.66, 912.83, 913.0, 913.18, 913.35, 913.53, 913.7, 913.88, 914.05, 914.23, 914.4, 914.58, 914.75, 914.92, 915.1, 915.27, 915.45, 915.62, 915.8, 915.97, 916.14, 916.32, 916.49, 916.67, 916.84, 917.02, 917.19, 917.36, 917.54, 917.71, 917.89, 918.06, 918.23, 918.41, 918.58, 918.76, 918.93, 919.1, 919.28, 919.45, 919.63, 919.8, 919.97, 920.15, 920.32, 920.49, 920.67, 920.84, 921.02, 921.19, 921.36, 921.54, 921.71, 921.88, 922.06, 922.23, 922.41, 922.58, 922.75, 922.93, 923.1, 923.27, 923.45, 923.62, 923.79, 923.97, 924.14, 924.31, 924.49, 924.66, 924.83, 925.01, 925.18, 925.35, 925.53, 925.7, 925.87, 926.05, 926.22, 926.39, 926.57, 926.74, 926.91, 927.09, 927.26, 927.43, 927.61, 927.78, 927.95, 928.13, 928.3, 928.47, 928.65, 928.82, 928.99, 929.16, 929.34, 929.51, 929.68, 929.86, 930.03, 930.2, 930.37, 930.55, 930.72, 930.89, 931.07, 931.24, 931.41, 931.58, 931.76, 931.93, 932.1, 932.27, 932.45, 932.62, 932.79, 932.96, 933.14, 933.31, 933.48, 933.65, 933.83, 934.0, 934.17, 934.34, 934.52, 934.69, 934.86, 935.03, 935.21, 935.38, 935.55, 935.72, 935.9, 936.07, 936.24, 936.41, 936.58, 936.76, 936.93, 937.1, 937.27, 937.45, 937.62, 937.79, 937.96, 938.13, 938.31, 938.48, 938.65, 938.82, 938.99, 939.17, 939.34, 939.51, 939.68, 939.85, 940.03, 940.2, 940.37, 940.54, 940.71, 940.88, 941.06, 941.23, 941.4, 941.57, 941.74, 941.91, 942.09, 942.26, 942.43, 942.6, 942.77, 942.94, 943.12, 943.29, 943.46, 943.63, 943.8, 943.97, 944.14, 944.32, 944.49, 944.66, 944.83, 945.0, 945.17, 945.34, 945.52, 945.69, 945.86, 946.03, 946.2, 946.37, 946.54, 946.71, 946.89, 947.06, 947.23, 947.4, 947.57, 947.74, 947.91, 948.08, 948.25, 948.42, 948.6, 948.77, 948.94, 949.11, 949.28, 949.45, 949.62, 949.79, 949.96, 950.13, 950.3, 950.48, 950.65, 950.82, 950.99, 951.16, 951.33, 951.5, 951.67, 951.84, 952.01, 952.18, 952.35, 952.52, 952.69, 952.86, 953.03, 953.21, 953.38, 953.55, 953.72, 953.89, 954.06, 954.23, 954.4, 954.57, 954.74, 954.91, 955.08, 955.25, 955.42, 955.59, 955.76, 955.93, 956.1, 956.27, 956.44, 956.61, 956.78, 956.95, 957.12, 957.29, 957.46, 957.63, 957.8, 957.97, 958.14, 958.31, 958.48, 958.65, 958.82, 958.99, 959.16, 959.33, 959.5, 959.67, 959.84, 960.01, 960.18, 960.35, 960.52, 960.69, 960.86, 961.03, 961.2, 961.37, 961.54, 961.71, 961.88, 962.05, 962.22, 962.39, 962.56, 962.73, 962.89, 963.06, 963.23, 963.4, 963.57, 963.74, 963.91, 964.08, 964.25, 964.42, 964.59, 964.76, 964.93, 965.1, 965.27, 965.43, 965.6, 965.77, 965.94, 966.11, 966.28, 966.45, 966.62, 966.79, 966.96, 967.13, 967.3, 967.46, 967.63, 967.8, 967.97, 968.14, 968.31, 968.48, 968.65, 968.82, 968.98, 969.15, 969.32, 969.49, 969.66, 969.83, 970.0, 970.17, 970.33, 970.5, 970.67, 970.84, 971.01, 971.18, 971.35, 971.52, 971.68, 971.85, 972.02, 972.19, 972.36, 972.53, 972.69, 972.86, 973.03, 973.2, 973.37, 973.54, 973.7, 973.87, 974.04, 974.21, 974.38, 974.55, 974.71, 974.88, 975.05, 975.22, 975.39, 975.56, 975.72, 975.89, 976.06, 976.23, 976.4, 976.56, 976.73, 976.9, 977.07, 977.24, 977.4, 977.57, 977.74, 977.91, 978.08, 978.24, 978.41, 978.58, 978.75, 978.91, 979.08, 979.25, 979.42, 979.59, 979.75, 979.92, 980.09, 980.26, 980.42, 980.59, 980.76, 980.93, 981.09, 981.26, 981.43, 981.6, 981.76, 981.93, 982.1, 982.27, 982.43, 982.6, 982.77, 982.94, 983.1, 983.27, 983.44, 983.61, 983.77, 983.94, 984.11, 984.27, 984.44, 984.61, 984.78, 984.94, 985.11, 985.28, 985.44, 985.61, 985.78, 985.95, 986.11, 986.28, 986.45, 986.61, 986.78, 986.95, 987.11, 987.28, 987.45, 987.61, 987.78, 987.95, 988.12, 988.28, 988.45, 988.62, 988.78, 988.95, 989.12, 989.28, 989.45, 989.62, 989.78, 989.95, 990.12, 990.28, 990.45, 990.62, 990.78, 990.95, 991.11, 991.28, 991.45, 991.61, 991.78, 991.95, 992.11, 992.28, 992.45, 992.61, 992.78, 992.94, 993.11, 993.28, 993.44, 993.61, 993.78, 993.94, 994.11, 994.27, 994.44, 994.61, 994.77, 994.94, 995.1, 995.27, 995.44, 995.6, 995.77, 995.93, 996.1, 996.27, 996.43, 996.6, 996.76, 996.93, 997.1, 997.26, 997.43, 997.59, 997.76, 997.92, 998.09, 998.26, 998.42, 998.59, 998.75, 998.92, 999.08, 999.25, 999.41, 999.58, 999.75, 999.91, 1000.08, 1000.24, 1000.41, 1000.57, 1000.74, 1000.9, 1001.07, 1001.23, 1001.4, 1001.57, 1001.73, 1001.9, 1002.06, 1002.23, 1002.39, 1002.56, 1002.72, 1002.89, 1003.05, 1003.22, 1003.38, 1003.55, 1003.71, 1003.88, 1004.04, 1004.21, 1004.37, 1004.54, 1004.7, 1004.87, 1005.03, 1005.2, 1005.36, 1005.53, 1005.69, 1005.86, 1006.02, 1006.19, 1006.35, 1006.52, 1006.68, 1006.85, 1007.01, 1007.18, 1007.34, 1007.5, 1007.67, 1007.83, 1008.0, 1008.16, 1008.33, 1008.49, 1008.66, 1008.82, 1008.99, 1009.15, 1009.31, 1009.48, 1009.64, 1009.81, 1009.97, 1010.14, 1010.3, 1010.47, 1010.63, 1010.79, 1010.96, 1011.12, 1011.29, 1011.45, 1011.62, 1011.78, 1011.94, 1012.11, 1012.27, 1012.44, 1012.6, 1012.76, 1012.93, 1013.09, 1013.26, 1013.42, 1013.58, 1013.75, 1013.91, 1014.08, 1014.24, 1014.4, 1014.57, 1014.73, 1014.9, 1015.06, 1015.22, 1015.39, 1015.55, 1015.71, 1015.88, 1016.04, 1016.21, 1016.37, 1016.53, 1016.7, 1016.86, 1017.02, 1017.19, 1017.35, 1017.51, 1017.68, 1017.84, 1018.0, 1018.17, 1018.33, 1018.5, 1018.66, 1018.82, 1018.99, 1019.15, 1019.31, 1019.48, 1019.64, 1019.8, 1019.97, 1020.13, 1020.29, 1020.46, 1020.62, 1020.78, 1020.94, 1021.11, 1021.27, 1021.43, 1021.6, 1021.76, 1021.92, 1022.09, 1022.25, 1022.41, 1022.57, 1022.74, 1022.9, 1023.06, 1023.23, 1023.39, 1023.55, 1023.72, 1023.88, 1024.04, 1024.2, 1024.37, 1024.53, 1024.69, 1024.85, 1025.02, 1025.18, 1025.34, 1025.51, 1025.67, 1025.83, 1025.99, 1026.16, 1026.32, 1026.48, 1026.64, 1026.81, 1026.97, 1027.13, 1027.29, 1027.46, 1027.62, 1027.78, 1027.94, 1028.1, 1028.27, 1028.43, 1028.59, 1028.75, 1028.92, 1029.08, 1029.24, 1029.4, 1029.56, 1029.73, 1029.89, 1030.05, 1030.21, 1030.38, 1030.54, 1030.7, 1030.86, 1031.02, 1031.19, 1031.35, 1031.51, 1031.67, 1031.83, 1032.0, 1032.16, 1032.32, 1032.48, 1032.64, 1032.8, 1032.97, 1033.13, 1033.29, 1033.45, 1033.61, 1033.77, 1033.94, 1034.1, 1034.26, 1034.42, 1034.58, 1034.74, 1034.91, 1035.07, 1035.23, 1035.39, 1035.55, 1035.71, 1035.87, 1036.04, 1036.2, 1036.36, 1036.52, 1036.68, 1036.84, 1037.0, 1037.17, 1037.33, 1037.49, 1037.65, 1037.81, 1037.97, 1038.13, 1038.29, 1038.46, 1038.62, 1038.78, 1038.94, 1039.1, 1039.26, 1039.42, 1039.58, 1039.74, 1039.9, 1040.07, 1040.23, 1040.39, 1040.55]
print len(wavelengths)

handle = context.openByVendorIDAndProductID(0x2457, 0x1022, skip_on_error=True)
if handle is None:
	print("try running with sudo")

handle.claimInterface(0) #default interface is 0, from lsusb.

#main stuff

print(handle.bulkWrite(1, '\x01')) #init message

integrationTime = 100000 # in microseconds
t_i = struct.pack('<I', integrationTime)

print("get basic info")
print(handle.bulkWrite(1, '\x05\x00')) # get id
print(handle.bulkRead(129, 512))

print(handle.bulkWrite(1, '\x05\x01')) # get 0th order wavelength coefficient
print(handle.bulkRead(129, 512))

print(handle.bulkWrite(1, '\x05\x16')) # get configuration
print(handle.bulkRead(129, 512))

print("set int time")
print(handle.bulkWrite(1, '\x02' + t_i))

print("get spectra:")
data = []
print(handle.bulkWrite(1, '\x09'))


for i in xrange(4):
	data.append(handle.bulkRead(134, 512))
for _ in xrange(11):
	data.append(handle.bulkRead(130, 512))
print("sync packet:\n")
print(handle.bulkRead(130, 1))

_data = []
print(len(data))
for j in xrange(len(data)):
	for i in xrange(256):
		x = data[j][2*i:(i+1)*2]
#		print len(x)
#		print x
		_data.append(struct.unpack('<h', x)[0])

for i in xrange(len(wavelengths)):
	print("{}: {}\n".format(wavelengths[i], _data[i]))

print(len(_data))

#f = open('.temp', 'w')
handle.releaseInterface(0)
handle.close()
#handle.exit()
